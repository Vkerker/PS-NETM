import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import integrate
from scipy.stats import chi2
from scipy.stats import kstwo

def NETM (data):
    m = pd.DataFrame(columns=data.columns, index = ['m2', 'm3', 'm4', 'm5', 'm6', 'm8', 'RMS'])
    A = pd.DataFrame(columns=data.columns)
    e = pd.DataFrame(columns=data.columns)
    sigA = pd.DataFrame(columns=data.columns)
    sigE = pd.DataFrame(columns=data.columns)
    confA = pd.DataFrame(columns=data.columns)
    confE = pd.DataFrame(columns=data.columns)
    n = len(data)

    for col in data.columns:
        arr = np.array(data[col])

        m.loc["m2", col] = np.mean((arr - np.mean(arr))**2)
        m.loc["m3", col] = np.mean((arr - np.mean(arr))**3)
        m.loc["m4", col] = np.mean((arr - np.mean(arr))**4)
        m.loc["m5", col] = np.mean((arr - np.mean(arr))**5)
        m.loc["m6", col] = np.mean((arr - np.mean(arr))**6)
        m.loc["m8", col] = np.mean((arr - np.mean(arr))**8)
        m.loc['RMS', col] = np.sqrt(m.loc["m2", col])

        A.loc[0, col] = round((np.sqrt(n * (n-1))/(n-2))*((m.loc["m3", col])/(m.loc["m2", col]**1.5)), 2)
        e.loc[0, col] = round(((n-1)*(n**2-2*n+3)*m.loc["m4", col])/(n*(n-2)*(n-3)*(m.loc["m2", col]**2)) - (3*(n-1)*(2*n-3))/(n*(n-2)*(n-3)) - 3, 2)
        sigA.loc[0, col] = round(np.sqrt((4*m.loc["m2", col]**2*m.loc["m6", col]-12*m.loc["m2", col]*m.loc["m3", col]*m.loc["m5", col]-24*m.loc["m2", col]**3*m.loc["m4", col]+9*m.loc["m3", col]**2*m.loc["m4", col]+35*m.loc["m2", col]**2*m.loc["m2", col]**3+36*m.loc["m2", col]**5)/(4*m.loc["m2", col]**5*n)), 2)
        sigE.loc[0, col] = round(np.sqrt((m.loc["m2", col]**2*m.loc["m8", col]-4*m.loc["m2", col]*m.loc["m4", col]*m.loc["m6", col]-8*m.loc["m2", col]**3*m.loc["m3", col]*m.loc["m5", col]+4*m.loc["m4", col]**3-m.loc["m2", col]**2*m.loc["m4", col]**2+16*m.loc["m2", col]*m.loc["m3", col]**2*m.loc["m4", col]+16*m.loc["m2", col]**3*m.loc["m3", col]**2)/(m.loc["m2", col]**6*n)),2)
        confA.loc[0, col] = round(A.loc[0, col]-1.645*sigA.loc[0, col], 2)
        confA.loc[1, col] = round(A.loc[0, col]+1.645*sigA.loc[0, col], 2)
        confE.loc[0, col] = round(e.loc[0, col]-1.645*sigE.loc[0, col], 2)
        confE.loc[1, col] = round(e.loc[0, col]+1.645*sigE.loc[0, col], 2)
    return(A, e, m, sigA, sigE, confA, confE, n)

def hist_data(data, n):
    intervals = pd.DataFrame(columns=data.columns)
    bars = pd.DataFrame(columns=data.columns)
    x_i = pd.DataFrame(columns=data.columns)
    m_i = pd.DataFrame(columns=data.columns)
    for col in data.columns:
        bins = round(1+3.322 * np.log10(n))
        fig, ax = plt.subplots()
        val, f_intervals, f_bars = ax.hist(data[col], bins=bins)
        bars[col] = ax.bar_label(f_bars)
        intervals[col] = f_intervals
    for col, value in bars.items():
        for idx, val in enumerate(value):
            xcoord, _ = val.xy
            x_i.loc[idx, col] = xcoord
            m_i.loc[idx, col] = int(val.get_text())
    return(intervals, x_i, m_i)

def standard_normal_cdf(t):
    return (1 / np.sqrt(2 * np.pi)) * integrate.quad(lambda x: np.exp(-x**2/2), 0, t)[0]

def chi2_right_tail_prob(chi2_val, df):
    p_val = 1 - chi2.cdf(chi2_val, df)
    return p_val

def kolmogorov_right_tail_prob(D_val, n):
    p_val = 1 - kstwo.cdf(D_val, n)
    return p_val

def p_criteria(x_i, m_i, n, interval):
    p_i = pd.DataFrame(columns=x_i.columns)
    ti = pd.DataFrame(columns=x_i.columns)
    chi = pd.DataFrame(np.zeros((1, len(x_i.columns))), columns=x_i.columns)
    m_x = pd.DataFrame(np.zeros((1, len(x_i.columns))) ,columns=x_i.columns)
    dispers = pd.DataFrame(np.zeros((1, len(x_i.columns))), columns=x_i.columns)
    for col, value in m_i.items():
        for idx, val in enumerate(value):
            p_i.loc[idx, col] = val/n

    for col, value in x_i.items():
        for idx, val in enumerate(value):
            m_x.loc[0, col] += val * p_i.loc[idx, col]
    
    for col, value in x_i.items():
        for idx, val in enumerate(value):
            dispers.loc[0, col] += ((val - m_x.loc[0, col])**2) * p_i.loc[idx, col]

    for col, value in interval.items():
        for idx, val in enumerate(value):
            if idx+1 < len(value):
                ti.loc[idx, col] = standard_normal_cdf((value[idx+1]-m_x.loc[0, col])/np.sqrt(dispers.loc[0, col]))-standard_normal_cdf((value[idx]-m_x.loc[0, col])/np.sqrt(dispers.loc[0, col]))
            else: break

    for col,value in ti.items():
        for idx, val in enumerate(value):
            ti.loc[idx, col] = round(ti.loc[idx, col] * n)

    for col, value in ti.items():
        for idx, val in enumerate(value):
            try:
                chi.loc[0, col] += (m_i.loc[idx, col] - ti.loc[idx, col])**2/ti.loc[idx, col]
            except ZeroDivisionError: continue
    for column in chi.columns:
        chi.loc[0, column] = round(chi2_right_tail_prob(chi.loc[0, column], (len(x_i)-3)), 2)
    return(chi, m_x, dispers)

def k_criteria(m_i, interval, n, m_x, dispers):
    F_stat = pd.DataFrame(columns=m_i.columns)
    F_theoret = pd.DataFrame(columns=m_i.columns)
    p_i = pd.DataFrame(columns=m_i.columns)
    D = pd.DataFrame(columns=m_i.columns)
    for col, value in m_i.items():
        for idx, val in enumerate(value):
            p_i.loc[idx, col] = val/n
    for col, value in interval.items():
        arr = np.array(p_i.loc[:, col])
        F_stat.loc[:, col] = np.cumsum(arr)
        for idx, val in enumerate(value):
            F_theoret.loc[idx, col] = (0.5 + standard_normal_cdf((val - m_x.loc[0, col])/np.sqrt(dispers.loc[0, col])))
    F_stat.loc[-1] = [0,0,0]
    F_stat.sort_index(inplace=True)
    F_stat.reset_index(drop=True, inplace=True)
    for col, value in F_stat.items():
        D.loc[0, col] = max(abs(val - F_theoret.loc[idx, col]) for idx, val in enumerate(value))
        D.loc[0, col] = round(kolmogorov_right_tail_prob(D.loc[0, col], n), 3)       
    return(D)