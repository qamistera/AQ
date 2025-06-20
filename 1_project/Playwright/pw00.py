from playwright.sync_api import sync_playwright, expect
import time


# Создаем экземпляр Playwright и запускаем его
playwright = sync_playwright().start()

# Далее, используя объект playwright, можно запускать браузер и работать с ним
browser = playwright.chromium.launch(headless=False, slow_mo=1000)
page =browser.new_page()
page.goto("https://www.saucedemo.com")
page.type(selector='[id="user-name"]', text="standard_user", delay=100)
page.fill(selector='#password', value="secret_sauce")
page.click(selector='.submit-button') #'[class="submit-button"]'
page.wait_for_selector('#inventory_container')
page.wait_for_url("https://www.saucedemo.com/inventory.html", timeout=10000)

button_add_cart= '[data-test="add-to-cart-sauce-labs-backpack"]' # '#add-to-cart-sauce-labs-backpack'
alt_locator_for_button= '.inventory_item a:has-text("Sauce Labs Backpack")'
cart_button= '.inventory_item_description:has-text("Sauce Labs Backpack") button:has-text("Add to cart")'

page.is_visible(selector=button_add_cart)  #'[data-test="add-to-cart-sauce-labs-backpack"]'
page.is_enabled(selector=button_add_cart)
#page.click(selector=button_add_cart)
#page.click(selector=alt_locator_for_button)
page.click(selector=cart_button)
page.is_visible('[data-test="shopping-cart-link"]')
page.click('[data-test="shopping-cart-link"]')
#page.wait_for_load_state('load')
page.wait_for_url("https://www.saucedemo.com/cart.html", timeout=10000)
button_checkout= '#checkout'
page.wait_for_selector(button_checkout)
page.is_visible(button_checkout)
page.is_enabled(button_checkout)
page.click(button_checkout)
page.wait_for_url("https://www.saucedemo.com/checkout-step-one.html", timeout=10000)
page.type(selector='[id="first-name"]', text="standard_user")
page.type(selector='[id="last-name"]', text="last")
page.fill(selector='[id="postal-code"]', value="333332")
page.click('[id="continue"][type="submit"]')
page.wait_for_url("https://www.saucedemo.com/checkout-step-two.html", timeout=10000)
page.click('#finish')



time.sleep(5)
browser.close()

playwright.stop()