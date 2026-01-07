from selenium import webdriver

print("=== ENVIRONMENT.PY TERLOAD ===")

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    context.driver = webdriver.Chrome(options)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()
