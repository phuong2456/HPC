def lu_det(a):
    determ = 1
    log_determ = 0
    for k in range(0,int(n/m)):
        P, L, U = scipy.linalg.lu(a)
        L_inv = np.linalg.inv(L)
        U_inv = np.linalg.inv(U)
        determ = determ * np.linalg.det(L)*np.linalg.det(U) 
        log_determ += log(abs((np.linalg.det(L)))) + log(abs((np.linalg.det(U))))
        for i in range((k+1),int(n/m)):
            a_mat_ik = a[i,k] * L_inv
            a_mat_ki = a[k,i] * U_inv
        for i in range((k+1),int(n/m)):
            for j in range((k+1),int(n/m)):
                a_mat_jk = a[i,j] - a[i,k] * a[k,j]
    return determ, log_determ