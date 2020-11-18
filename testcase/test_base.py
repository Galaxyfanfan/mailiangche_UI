from page.base.app import APP


class TestBase():
    def setup(self):
        self.app = APP()
        self.app.start()

    def teardown(self):
        self.app.stop()