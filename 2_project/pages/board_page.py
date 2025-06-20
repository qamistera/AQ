from playwright.sync_api import expect
import allure
from faker import Faker
from pages.base_page import BasePage


class BoardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = "90151280260/v/l/2kypyqm4-275"
        self.faker = Faker()

    # Селекторы действий на доске
    ADD_TASK_BUTTON = "button[data-test='create-task-menu__new-task-button']"  # кнопка "+ Add task"
    TASK_NAME_INPUT = 'textarea[data-test="draft-view__title-task"]'          # поле ввода названия задачи
    TASK_DESC_TRIGGER = '[data-test="dropdown-list-item__Add description"]'  # клик по "Add description"
    TASK_DESC_INPUT = ".ql-editor"                                          # поле для ввода описания
    CONFIRM_TASK_BUTTON = '[data-test="draft-view__quick-create-create"]'  # кнопка "Create task"

    @allure.step("Создаём задачу с автогенерацией имени и описания")
    def create_fake_task(self):
        task_name = self.faker.sentence(nb_words=4)
        description = self.faker.text(max_nb_chars=100)

        self.open()
        self.wait_for_selector_and_click(self.ADD_TASK_BUTTON)  # нажимаем "+ Add task"
        self.wait_for_selector_and_type(self.TASK_NAME_INPUT, task_name, delay=50)  # вводим название задачи
        self.wait_for_selector_and_click(self.TASK_DESC_TRIGGER)  # кликаем на "Add description"
        self.wait_for_selector_and_type(self.TASK_DESC_INPUT, description, delay=50)  # вводим описание задачи
        self.wait_for_selector_and_click(self.CONFIRM_TASK_BUTTON)  # нажимаем "Create task"
        self.page.wait_for_timeout(1000)

        task_link = self.page.locator(f"a:has-text('{task_name}')")
        href = task_link.get_attribute("href")

        if not href or "/t/" not in href:
            raise Exception("Не удалось извлечь task_id из href задачи")

        task_id = href.split("/t/")[1]
        return task_name, task_id

    @allure.step("Проверяем, что задача появилась: {task_name}")
    def assert_task_created(self, task_name: str):
        self.assert_text_present_on_page(task_name)  # проверка по тексту задачи в DOM

    @allure.step("Удаляем задачу по имени через UI")
    def delete_task_ui(self, task_name):
        # Открываем меню конкретной задачи
        task_container = self.page.get_by_test_id(f"task-row__container__{task_name}")
        task_container.locator('[data-test="task-row-menu__ellipsis-v3-button"]').click()

        # Нажимаем "Delete task" — сразу удаляет
        self.page.locator('[data-test="quick-actions-menu__delete-task"]').click()

        # Даём немного времени на удаление
        self.page.wait_for_timeout(1000)

        # Проверяем, что задача больше не отображается
        expect(self.page.locator(f"text={task_name}")).not_to_be_visible()