import numpy as np

def xyz_to_neu(df):
    a = 6378137.0
    alpha = 1/298.257
    e2 = 2*alpha-alpha**2
    c = 1 / 1 - e2

    last_row = df.iloc[-1]
    X_ref, Y_ref, Z_ref = last_row['x'], last_row['y'], last_row['z']
    R = np.sqrt(X_ref**2 + Y_ref**2)
    b = a * e2 / R * np.sqrt(1 - e2)
    phi_i = np.arctan2(Z_ref, R)
    i = 0
    while True:
        phi_i1 = np.arctan((Z_ref / R) + (b * np.tan(phi_i)) / np.sqrt(c + np.tan(phi_i)**2))
        i+=1
        if i == 4:
            phi_ref = phi_i1
            break
        phi_i = phi_i1
    lambda_ref = np.arctan2(Y_ref, X_ref)

    sin_phi = np.sin(phi_ref)
    cos_phi = np.cos(phi_ref)
    sin_lambda = np.sin(lambda_ref)
    cos_lambda = np.cos(lambda_ref)
    transformation_matrix = np.array([[-sin_phi * cos_lambda, -sin_phi * sin_lambda, cos_phi],
                                      [-sin_lambda, cos_lambda, 0],
                                      [cos_phi * cos_lambda, cos_phi * sin_lambda, sin_phi]])

    delta_xyz = df.iloc[:,:3] - [X_ref, Y_ref, Z_ref]
    topocentric_coords = round(delta_xyz @ transformation_matrix, 4)
    topocentric_coords.columns = ['N', 'E', 'U']
    
    return topocentric_coords