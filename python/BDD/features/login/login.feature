# File ini digunakan untuk menyimpan gherkin Fitur Login
Feature: Login OrangeHRM

  Scenario: Login sukses
    Given user membuka halaman login
    When user login menggunakan data "valid_user"
    Then user berhasil masuk ke "Dashboard"

  Scenario: Login gagal - password salah
    Given user membuka halaman login
    When user login menggunakan data "invalid_password"
    Then muncul pesan error "Invalid credentials"

  Scenario: Login gagal - username kosong
    Given user membuka halaman login
    When user login menggunakan data "empty_username"
    Then muncul pesan error field "Required"

  Scenario: Login gagal - password kosong
    Given user membuka halaman login
    When user login menggunakan data "empty_password"
    Then muncul pesan error field "Required"
