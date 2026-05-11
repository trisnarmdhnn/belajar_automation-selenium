# File ini digunakan untuk menyimpan gherkin Fitur Login

@login #merupakan sebuah tag yang berfungsi untuk memanggil function login pada file environment
Feature: Navigasi

  Scenario: Membuka halaman Admin
    Given user berada di halaman "Dashboard"
    When user klik navigasi admin
    Then user berhasil membuka halaman "Admin"

  Scenario: Membuka halaman PIM
    Given user berada di halaman "Dashboard"
    When user klik navigasi pim
    Then user berhasil membuka halaman "PIM"

  Scenario: Membuka halaman Leave
    Given user berada di halaman "Dashboard"
    When user klik navigasi leave
    Then user berhasil membuka halaman "Leave"