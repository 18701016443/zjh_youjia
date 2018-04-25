#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2018/3/10 10:08
"""
# 线上线索CooperationID6321 站点传selectsite（4）
#测试站点CooperationID737    站点传selectsite（11）

from test_cases.page_obj import ownerH5_page,login_page,cooperation_page,contract_page,housemanagelist_page,leaguelist_page,nav_page,roomdetails_page,softoutfit_page,writeleague_page
from models import myunit,mydef
from time import sleep
import unittest,os



class TestData(myunit.MyTest):

    def test_createData(self):
        #H5发布线索
        H5 = ownerH5_page.OwnerH5(self.driver)
        sleep(2)
        H5.openH5()
        sleep(1)
        H5.Owner()
        sleep(1)
        H5.OwnerName()
        sleep(1)
        H5.OwnerPhone()
        sleep(1)
        H5.OwnerPicture()
        sleep(1)
        H5.OwnerMessageInput()
        sleep(1)
        H5.OwnerMessage()
        sleep(1)
        H5.OwnerResidence()
        sleep(1)
        H5.OwnerRoomNum()
        sleep(1)
        H5.Province()
        sleep(1)
        H5.xiugai("province_select")
        sleep(2)
        H5.xinjiang()
        sleep(1)
        H5.xiugai("city_select")
        sleep(1)
        H5.wujiaqu()
        sleep(1)
        H5.qu()
        sleep(1)
        H5.Address()
        sleep(1)
        H5.SubmitBtn()
        sleep(2)

        #登录 AND 筛选线索ID
        login_page.LoginPage(self.driver).Login()
        sleep(2)
        nav_page.NavPage(self.driver).jichufuwu()
        sleep(2)
        nav_page.NavPage(self.driver).LeagueManage()

        #传参数线索ID
        #测试环境：①五家渠线索：737
        #          ②北京昌平线索：756
        #          ③上海线索：757
        #线上环境：线索ID：6321，13918
        cooperation_page.CooperationPage(self.driver).CooperationID(13918)
        sleep(2)
        cooperation_page.CooperationPage(self.driver).wujiaqu()
        sleep(2)
        cooperation_page.CooperationPage(self.driver).Serch()
        sleep(2)

        #发起签约
        cooperation_page.CooperationPage(self.driver).StartLeague()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).LeagueMoney(100)
        writeleague_page.WriteLeague(self.driver).ServiceCharge(1)
        sleep(2)
        writeleague_page.WriteLeague(self.driver).Proportions(1)
        sleep(2)
        writeleague_page.WriteLeague(self.driver).WTServicePeriodStart()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).WTServicePeriodEnd()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).Submit()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).LeagueRoomYes()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).DocumentTypePOC()
        sleep(2)

        # 点击上传图片
        writeleague_page.WriteLeague(self.driver).DocumentTypePhoto()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).AutoIt()
        sleep(2)

        # 选择房屋类型
        writeleague_page.WriteLeague(self.driver).RoomType()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).selectType()
        sleep(2)

        # 填写室、卫、厅、厨、阳台、建筑面积、楼层
        writeleague_page.WriteLeague(self.driver).RoomNum()
        sleep(1)
        writeleague_page.WriteLeague(self.driver).Parlor()
        sleep(1)
        writeleague_page.WriteLeague(self.driver).Toilet()
        sleep(1)
        writeleague_page.WriteLeague(self.driver).Kitchen()
        sleep(1)
        writeleague_page.WriteLeague(self.driver).Balcony()
        sleep(1)
        writeleague_page.WriteLeague(self.driver).Area()
        sleep(1)
        writeleague_page.WriteLeague(self.driver).Floor()
        sleep(1)
        writeleague_page.WriteLeague(self.driver).DetailedAddress()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).Residentialquarters()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).DoorNumbe()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).maodian()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).Submit()


        #加盟列表筛选数据
        nav_page.NavPage(self.driver).LeagueApplyList()
        sleep(1)
        leaguelist_page.LeagueList(self.driver).Phone(18701016443)
        sleep(2)
        leaguelist_page.LeagueList(self.driver).wujiaqu()
        sleep(3)
        leaguelist_page.LeagueList(self.driver).Serach()
        sleep(2)

        #分配站点（重点！！！重点！！！重点！！！）
        po = leaguelist_page.LeagueList(self.driver)
        if po.LeagueState() == "待审核":
            sleep(2)
            po.LeagueDetails()
            sleep(2)
            po.Pass()
            sleep(1)
            po.SiteAlert()
            sleep(3)
            #分配站点（一定要注意数据的准确性）
            #测试环境：①北京昌平站：1
            #          ②五家渠站点：38
            #          ③上海站点：2
            #线上环境：五家渠站点（12）：3
            po.selectsite("3")
            sleep(2)
            po.ConfirmBtn()
            sleep(1)
        else:
            print("状态不对")



        #编辑合同
        nav_page.NavPage(self.driver).LeagueApplyList()
        sleep(2)
        leaguelist_page.LeagueList(self.driver).Phone(18701016443)
        sleep(2)
        leaguelist_page.LeagueList(self.driver).wujiaqu()
        sleep(2)
        leaguelist_page.LeagueList(self.driver).Serach()
        sleep(2)
        leaguelist_page.LeagueList(self.driver).EidtContract()
        sleep(2)
        contract_page.Contract(self.driver).Edit()
        sleep(2)
        contract_page.Contract(self.driver).ContractID()
        sleep(2)
        contract_page.Contract(self.driver).ContractPhoto()
        sleep(2)
        os.system("D:/python/youjia/data/up.exe")
        sleep(1)
        contract_page.Contract(self.driver).FirstParty()
        sleep(2)
        contract_page.Contract(self.driver).IDcard()
        sleep(2)
        contract_page.Contract(self.driver).Address()
        sleep(2)
        contract_page.Contract(self.driver).phone()
        sleep(2)
        contract_page.Contract(self.driver).Email()
        sleep(2)

        contract_page.Contract(self.driver).DocumentNumber()
        sleep(2)
        contract_page.Contract(self.driver).ProofPeople()

        sleep(2)
        contract_page.Contract(self.driver).ServiceDataStart()
        sleep(1)
        contract_page.Contract(self.driver).ServiceDataEnd()
        sleep(2)
        contract_page.Contract(self.driver).SoftContract()
        sleep(1)
        contract_page.Contract(self.driver).OperationUpgradeFee(1)
        sleep(1)
        contract_page.Contract(self.driver).SoftPic()
        sleep(1)
        contract_page.Contract(self.driver).BedBuy()
        sleep(1)
        contract_page.Contract(self.driver).BedFee(1)
        # contract_page.Contract(self.driver).SoftDeposit()
        sleep(1)
        contract_page.Contract(self.driver).Card()
        sleep(1)
        contract_page.Contract(self.driver).UpgradeCost()
        sleep(1)
        # contract_page.Contract(self.driver).Card()

        #床垫租赁
        # contract_page.Contract(self.driver).BedLease()
        # sleep(2)
        # num = mydef.rad_num(1,100)
        # contract_page.Contract(self.driver).BedLeaseNum(num)
        # sleep(2)
        # pic = mydef.rad_num(0,1000)
        # contract_page.Contract(self.driver).BedLeasePic(pic)
        # sleep(1)

        contract_page.Contract(self.driver).SoftContractUp()
        sleep(2)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)
        contract_page.Contract(self.driver).SubmissionOfAudit()
        sleep(2)
        contract_page.Contract(self.driver).ConfirmBtn()
        sleep(2)
        contract_page.Contract(self.driver).Pass()
        sleep(2)
        contract_page.Contract(self.driver).AlertPass()
        sleep(2)

        # 确认收款步骤
        cc = contract_page.Contract(self.driver)
        cc.PassPayment()
        sleep(2)
        cc.PaymentAlert()
        sleep(2)
        cc.SoftContractPic()
        sleep(2)
        cc.SoftContractPicAlert()
        sleep(2)

        #完成保洁
        nav_page.NavPage(self.driver).jichufuwu()
        sleep(1)
        nav_page.NavPage(self.driver).RoomManage()
        sleep(1)
        nav_page.NavPage(self.driver).HouseManage()
        sleep(1)
        housemanagelist_page.HouseManagePage(self.driver).wujiaqu()
        sleep(2)
        housemanagelist_page.HouseManagePage(self.driver).FinishCleaning()
        sleep(2)
        housemanagelist_page.HouseManagePage(self.driver).PassBtn()
        sleep(1)

        #编辑房屋
        housemanagelist_page.HouseManagePage(self.driver).list_HouseID()
        sleep(2)
        housemanagelist_page.HouseManagePage(self.driver).EditHouse()
        sleep(1)

        # 房屋标题
        title = "张佳恒测试" + mydef.rad_word(2)
        housemanagelist_page.HouseManagePage(self.driver).HouseTitle(title)
        sleep(1)

        # 房屋简介
        Abbreviation = "这是一个测试房屋"
        housemanagelist_page.HouseManagePage(self.driver).HouseNickAbbreviation(Abbreviation)
        sleep(1)

        # 淋浴数量
        shower = "2"
        housemanagelist_page.HouseManagePage(self.driver).Shower(shower)
        sleep(1)

        # 床的数量
        bed = "2"
        housemanagelist_page.HouseManagePage(self.driver).SingleBed(bed)
        sleep(1)

        # 上传封面照片
        housemanagelist_page.HouseManagePage(self.driver).Cover()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)
        housemanagelist_page.HouseManagePage(self.driver).Parlour()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)
        housemanagelist_page.HouseManagePage(self.driver).Bedroom()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)
        housemanagelist_page.HouseManagePage(self.driver).Kitchen()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)
        housemanagelist_page.HouseManagePage(self.driver).Bathroom()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)
        housemanagelist_page.HouseManagePage(self.driver).Other()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)
        housemanagelist_page.HouseManagePage(self.driver).submitBtn()
        sleep(1)

if __name__ == "__main__":
    unittest.main()
