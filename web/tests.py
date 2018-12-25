# from django.test import TestCase

# # Create your tests here.
# import time
# from web.seleniumapi import SeleniumApi
# from web.TestCaseInfo import TestCaseInfo
# from web.TestReport import TestReport
# # import .Util.logger_config
# from django.test import LiveServerTestCase
# class Test(LiveServerTestCase):

#     def setUp(self):
#         self.testcaseinfo = TestCaseInfo(id="3",name="Login to floor manager lite using sbxadmin",owner="xua")
#         self.testResult = TestReport()
#         self.testcaseinfo.starttime = str(time.asctime())
#         SeleniumApi.step_startup(self)
#         print("调用开始")

#     def test_animals_can_speak(self):
#         try:
#             SeleniumApi.step_send_keys(self,"//input[@id = 'kw']",'behave')
#             time.sleep(1)
#             SeleniumApi.step_click(self,"//input[@id = 'su']") 
#             time.sleep(10)
#             self.testcaseinfo.result = "Pass"
#         except Exception as err:
#             self.testcaseinfo.errorinfo = str(err)
#             # Util.loggerconfig.initLogging(self,err)

#         finally:
#             self.testcaseinfo.endtime = str(time.asctime())

#     def tearDown(self):
#         if '百度为您找到相关结果约' in SeleniumApi.step_text(self,"div.nums"):
#             assert True  
#         else:
#             assert False
#         SeleniumApi.step_quit(self)
#         self.testResult.WriteHTML(self.testcaseinfo)
#         self.testResult.WriteResult(self.testcaseinfo)


