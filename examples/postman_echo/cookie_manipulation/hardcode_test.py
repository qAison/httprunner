# NOTE: Generated By HttpRunner v4.0.0
# FROM: cookie_manipulation/hardcode.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseHardcode(HttpRunner):

    config = (
        Config("set & delete cookies.")
        .base_url("https://postman-echo.com")
        .verify(False)
        .export(*["cookie_foo1"])
    )

    teststeps = [
        Step(
            RunRequest("set cookie foo1 & foo2 & foo3")
            .get("/cookies/set")
            .with_params(**{"foo1": "bar1", "foo2": "bar2"})
            .with_headers(**{"User-Agent": "HttpRunner/${get_httprunner_version()}"})
            .extract()
            .with_jmespath("body.cookies.foo1", "cookie_foo1")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.cookies.foo1", "bar1")
            .assert_equal("body.cookies.foo2", "bar2")
        ),
        Step(
            RunRequest("delete cookie foo2")
            .get("/cookies/delete?foo2")
            .with_headers(**{"User-Agent": "HttpRunner/${get_httprunner_version()}"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.cookies.foo1", "bar1")
            .assert_equal("body.cookies.foo2", None)
        ),
    ]


if __name__ == "__main__":
    TestCaseHardcode().test_start()