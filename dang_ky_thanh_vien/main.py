import sys
import os

# --- SỬA LỖI KHỞI ĐỘNG COCOA TRÊN MAC ---
try:
    import PyQt5
    if hasattr(PyQt5, '__file__') and PyQt5.__file__ is not None:
        dirname = os.path.dirname(PyQt5.__file__)
        plugin_path = os.path.join(dirname, 'Qt5', 'plugins', 'platforms')
        if os.path.exists(plugin_path):
            os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
except Exception:
    pass
# ----------------------------------------

# THAY THẾ QTPY BẰNG PYQT5 TRỰC TIẾP ĐỂ TRÁNH LỖI BINDINGS
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from connect_dtb import get_db_connection
from validation import kiem_tra_mat_khau_manh


class Main_Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main_Ui, self).__init__()

        # Tự động lấy đường dẫn tuyệt đối động để tìm file register.ui
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, 'register.ui')
        uic.loadUi(ui_path, self)

        # === TỰ ĐỘNG SINH ĐẦY ĐỦ NGÀY, THÁNG, NĂM ===
        self.cb_ngay.clear()
        self.cb_thang.clear()
        self.cb_nam.clear()

        # Tạo ngày từ 1 đến 31
        for d in range(1, 32):
            self.cb_ngay.addItem(str(d))

        # Tạo tháng từ 1 đến 12
        for m in range(1, 13):
            self.cb_thang.addItem(str(m))

        # Tạo năm từ 2026 lùi về 1950
        for y in range(2026, 1949, -1):
            self.cb_nam.addItem(str(y))
        # ============================================

        self.show()
        self.btn_register.clicked.connect(self.btn_register_click)

    def btn_register_click(self):
        ho = self.txt_ho.text().strip()
        ten = self.txt_ten.text().strip()
        contact = self.txt_contact.text().strip()
        password = self.txt_password.text().strip()

        ngay = self.cb_ngay.currentText()
        thang = self.cb_thang.currentText()
        nam = self.cb_nam.currentText()
        ngay_sinh = f"{nam}-{thang}-{ngay}"

        gioi_tinh = ""
        if self.rad_nam.isChecked():
            gioi_tinh = "Nam"
        elif self.rad_nu.isChecked():
            gioi_tinh = "Nữ"
        elif self.rad_tuy_chinh.isChecked():
            gioi_tinh = "Tùy chỉnh"

        dong_y = self.chk_agree.isChecked()

        if ho == "" or ten == "" or contact == "" or password == "":
            QMessageBox.warning(self, "Lỗi", "Bạn bắt buộc phải nhập đầy đủ các trường thông tin!")
            return
        if dong_y == False:
            QMessageBox.warning(self, "Lỗi", "Bạn phải tích chọn đồng ý với các điều khoản!")
            return
        if gioi_tinh == "":
            QMessageBox.warning(self, "Lỗi", "Bạn phải chọn giới tính!")
            return
        if kiem_tra_mat_khau_manh(password) == False:
            QMessageBox.warning(self, "Lỗi",
                                "Mật khẩu yếu! Phải có ít nhất 8 ký tự, gồm 1 chữ thường, 1 chữ hoa, 1 số và 1 ký tự đặc biệt.")
            return

        conn = get_db_connection()
        if conn is None:
            QMessageBox.critical(self, "Lỗi kết nối", "Không kết nối được database!")
            return

        try:
            cursor = conn.cursor()
            sql = "INSERT INTO users (ho, ten, sdt_hoac_email, mat_khau, ngay_sinh, gioi_tinh) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (ho, ten, contact, password, ngay_sinh, gioi_tinh)

            cursor.execute(sql, val)
            conn.commit()

            QMessageBox.information(self, "Thành công", "Đăng ký thành công!")

            self.txt_ho.clear()
            self.txt_ten.clear()
            self.txt_contact.clear()
            self.txt_password.clear()
            self.chk_agree.setChecked(False)

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Lỗi SQL", f"Đã có lỗi xảy ra: {e}")


app = QtWidgets.QApplication(sys.argv)
window = Main_Ui()
app.exec_()