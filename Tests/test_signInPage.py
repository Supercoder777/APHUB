from Utilities.Foundation import Foundation
import pytest


class TestSignInPage(Foundation):
    def test_loginData(self,getData):
        log = self.getlogger()
        signInPage = signInPage(self.driver)
        signInPage.getEmail().send_keys(getData[""])
        signInPage.getPassword().send_keys(getData{""})
        signInPage.submit().click()

        Assert

