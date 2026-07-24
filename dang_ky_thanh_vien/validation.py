def kiem_tra_mat_khau_manh(mat_khau):
    if len(mat_khau) < 8:
        return False

    co_chu_thuong = False
    co_chu_hoa = False
    co_so = False
    co_ky_tu_dac_biet = False

    ky_tu_dac_biet = "@$!%*?&"

    for ky_tu in mat_khau:
        if ky_tu.islower():
            co_chu_thuong = True
        elif ky_tu.isupper():
            co_chu_hoa = True
        elif ky_tu.isdigit():
            co_so = True
        elif ky_tu in ky_tu_dac_biet:
            co_ky_tu_dac_biet = True

    if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet:
        return True
    else:
        return False