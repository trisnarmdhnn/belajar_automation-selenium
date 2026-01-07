from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pytest

# ===== SESI PERTAMA ===== #
# untuk menjalankan pytest, code perlu dimasukan ke dalam sebuah class
# run all testcases = pytest {namafile}.py
# run one testcase = pytest {nama_file}::{nama_function/testcase}

#fixture digunakan agar ketika terjadi failed pada suatu case, code atau function setelahnya tetap di jalankan
@pytest.fixture
def driver():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)

    #Open browser and website
    driver = webdriver.Chrome(option)
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    
    #yield adalah perintah yang berguna untuk agar ketika function sudah selesai digunakan makan akan di kembalikan
    yield driver
    driver.quit()

def test_login_positif(driver):
    #wait - implicitly
    #driver.implicitly_wait(10)

    #wait - explicitly
    waitElementVisible = WebDriverWait(driver, timeout=10)
    username = waitElementVisible.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]')))

    #username = driver.find_element(By.XPATH, '//input[@name="username"]')
    username.send_keys('Admin')

    password = driver.find_element(By.XPATH, '//input[@name="password"]')
    password.send_keys('admin123' + Keys.ENTER)

    # btnLogin = driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    driver.implicitly_wait(10)

    HeaderDasboard = driver.find_element(By.XPATH, '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]')
    Username = driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]')

    #Melakukan Verifikasi
    assert "Dashboard" in HeaderDasboard.text
    assert "manda user" in Username.text


def test_login_negatif_invalid_password(driver): 
    #wait - explicitly
    waitElementVisible = WebDriverWait(driver, timeout=10)
    username = waitElementVisible.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]')))

    #username = driver.find_element(By.XPATH, '//input[@name="username"]')
    username.send_keys('Admin')

    password = driver.find_element(By.XPATH, '//input[@name="password"]')
    password.send_keys('admin')

    btnLogin = driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    driver.implicitly_wait(10)

    errorCred = driver.find_element(By.XPATH, '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')

    assert errorCred.text == "Invalid credentials"
    
    
def test_login_negatif_username_is_null(driver):
    waitElementVisible = WebDriverWait(driver, timeout=10)
    username = waitElementVisible.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]')))
    
    password = driver.find_element(By.XPATH, '//input[@name="password"]')
    password.send_keys('admin')
    
    btnLogin = driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    driver.implicitly_wait(10)

    errorUsernameNull = driver.find_element(By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"]')

    assert errorUsernameNull.text == "Required"
    
def test_login_negatif_password_is_null(driver):
    waitElementVisible = WebDriverWait(driver, timeout=10)
    username = waitElementVisible.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]')))
    username.send_keys('Admin')
    
    btnLogin = driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    driver.implicitly_wait(10)

    errorPasswordNull = driver.find_element(By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"]')

    assert errorPasswordNull.text == "Required"    
# ======================== #

# ===== SESI KEDUA ===== #




# ====================== #