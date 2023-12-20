import numpy as np
import pandas as pd
import pywt
import PyEMD
#<------------------------- REMOVE OUTLIERS ------------------------->

#Removes outliers, using modified z-score method

def remove_outliers(data):
    threshold = 2.5
    for col in data.columns:
        median = np.median(data[col])
        median_abs_deviation = np.median(np.abs(data[col] - median))
        modified_z_score = 0.6745 * (data[col] - median) / median_abs_deviation
        data = data.drop(data[abs(modified_z_score) > threshold].index)
    return data

#<------------------------- REMOVE TREND ------------------------->
#Removes trend, using first-order polynominal regression

def remove_secular_trend(data):
    data = data.copy()

    time = (data.index - data.index[0]).days
    trend_param = {}

    for column in data.columns:
        trend = np.polyfit(time, data[column], 1)
        data[column] = round(data[column] - (trend[0] * time + trend[1]), 4)
        trend_param[column] = {"slope": trend[0]} #Returns station speed in each direction

    return data, trend_param

#<------------------------- REMOVE NOISE (Wavelet Filter) ------------------------->

#Reduces noise effect on TS
#Denoising is performed on each component (N, E, U) seperately

def wavelet_denoise(df, wt, lvl):
    wavelet = wt
    level = lvl
    signal = df.values.T

    denoised_cols = []
    for c in range(signal.shape[0]):
        coeffs = pywt.wavedec(signal[c], wavelet, level=level)

        coeffs[1:] = [pywt.threshold(coef, value=0.5, mode='hard') for coef in coeffs[1:]]

        denoised_signal = pywt.waverec(coeffs, wavelet)[:len(df)]
        denoised_cols.append(denoised_signal)

    denoised_df = pd.DataFrame(data=np.array(denoised_cols).T, columns=df.columns, index=df.index)
    return denoised_df

#<------------------------- REMOVE NOISE (EMD Filter) ------------------------->
#Alternative method of denoising
#Note, that wavelet filter has shown better performance after some testing

def emd_denoise(dataframe):

    time = dataframe.index
    N = dataframe['N'].values
    E = dataframe['E'].values
    U = dataframe['U'].values

    emd = PyEMD.EMD()

    IMF_N = emd.emd(N, time)
    IMF_E = emd.emd(E, time)
    IMF_U = emd.emd(U, time)

    denoised_N = np.sum(IMF_N[1:], axis=0)
    denoised_E = np.sum(IMF_E[1:], axis=0)
    denoised_U = np.sum(IMF_U[1:], axis=0)
    
    denoised_dataframe = pd.DataFrame({'N': denoised_N, 'E': denoised_E, 'U': denoised_U}, index=dataframe.index)
    
    return denoised_dataframe
