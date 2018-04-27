#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2018/3/10 10:08
"""
"""
    重点：
    1、线上、预览线索CooperationID:13918 站点传selectsite（"3"）
    2、base文件修改mis地址，ownerH5_page修改H5地址

"""

from test_cases.page_obj import ownerH5_page,login_page,cooperation_page,contract_page,housemanagelist_page,leaguelist_page,nav_page,roomdetails_page,softoutfit_page,writeleague_page,roommanagelist_page
from models import myunit,mydef,configdb
from time import sleep
import unittest,os



class TestData(myunit.MyTest):

    def test_createData(self):

        # #H5发布线索
        # H5 = ownerH5_page.OwnerH5(self.driver)
        # sleep(2)
        #
        # #打开H5招募网页
        # H5.openH5()
        # sleep(1)
        #
        # #点击成为业主
        # H5.Owner()
        # sleep(1)
        #
        # #输入业主姓名
        # H5.OwnerName()
        # sleep(1)
        #
        # #输入业主手机号
        # H5.OwnerPhone()
        # sleep(1)
        #
        # #输入图片验证码
        # H5.OwnerPicture()
        # sleep(1)
        #
        # #点击发送短信按钮
        # H5.OwnerMessage()
        # sleep(3)
        #
        # # 从数据库查询获取短信
        # msg = configdb.cord(18701016443)
        # sleep(1)
        #
        # #输入短信验证码
        # H5.OwnerMessageInput(msg)
        # sleep(1)
        #
        # #选择房源类型，随机选择的
        # H5.OwnerResidence()
        # sleep(1)
        #
        # #房源套数，随机输入，范围1-999
        # H5.OwnerRoomNum()
        # sleep(1)
        #
        # #选择省份
        # H5.Province()
        # sleep(1)
        #
        # #利用js，将省份下拉框滚动到最底部，让“新疆”可点击
        # H5.xiugai("province_select")
        # sleep(2)
        #
        # #点击选择新疆
        # H5.xinjiang()
        # sleep(1)
        #
        # #利用js，将市下拉框滚动到最底部，让“五家渠”可点击
        # H5.xiugai("city_select")
        # sleep(1)
        #
        # #点击选择五家渠
        # H5.wujiaqu()
        # sleep(1)
        #
        # #点击选择区
        # H5.qu()
        # sleep(1)
        #
        # #输入详情地址
        # H5.Address()
        # sleep(1)
        #
        # #提交
        # H5.SubmitBtn()
        # sleep(2)


        #MIS登录
        login_page.LoginPage(self.driver).Login()
        sleep(2)

        #选择左侧基础服务
        nav_page.NavPage(self.driver).jichufuwu()
        sleep(2)

        #选择加盟管理
        nav_page.NavPage(self.driver).LeagueManage()

        #传参数线索ID
        #测试环境：①五家渠线索：737
        #          ②北京昌平线索：756
        #          ③上海线索：757
        #线上环境：线索ID：6321，13918
        cooperation_page.CooperationPage(self.driver).CooperationID(13918)
        sleep(2)

        #去掉五家渠，让五家渠数据可以显示
        cooperation_page.CooperationPage(self.driver).wujiaqu()
        sleep(2)

        #点击查询
        cooperation_page.CooperationPage(self.driver).Serch()
        sleep(2)

        #发起签约
        cooperation_page.CooperationPage(self.driver).StartLeague()
        sleep(2)

        #输入品牌使用费
        writeleague_page.WriteLeague(self.driver).LeagueMoney(100)
        sleep(1)

        #输入管理服务费
        writeleague_page.WriteLeague(self.driver).ServiceCharge(1)
        sleep(1)

        #输入有家分成比例
        writeleague_page.WriteLeague(self.driver).Proportions(1)
        sleep(2)

        #选择委托服务期限_开始时间
        writeleague_page.WriteLeague(self.driver).WTServicePeriodStart()
        sleep(2)

        #选择委托服务期限_结束时间
        writeleague_page.WriteLeague(self.driver).WTServicePeriodEnd()
        sleep(2)

        #时间插件没有收回去，如果没有收回去可能会遮住后面的定位，因此点击下提交按钮
        writeleague_page.WriteLeague(self.driver).Submit()
        sleep(2)

        #输入预期短租月收益
        writeleague_page.WriteLeague(self.driver).ExpectProfit()
        sleep(1)

        #输入长租月租金
        writeleague_page.WriteLeague(self.driver).LongMonthlyRent()
        sleep(2)

        #选择是加盟者本人房产
        writeleague_page.WriteLeague(self.driver).LeagueRoomYes()
        sleep(2)

        #选择房产证
        writeleague_page.WriteLeague(self.driver).DocumentTypePOC()
        sleep(2)

        # 点击上传图片
        writeleague_page.WriteLeague(self.driver).DocumentTypePhoto()
        sleep(2)

        #调用Auto上传图片
        writeleague_page.WriteLeague(self.driver).AutoIt()
        sleep(2)

        # 选择房屋类型——民居
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

        #输入详细地址——街道地址、小区、楼
        writeleague_page.WriteLeague(self.driver).DetailedAddress()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).Residentialquarters()
        sleep(2)
        writeleague_page.WriteLeague(self.driver).DoorNumbe()
        sleep(2)

        #地图扎点
        writeleague_page.WriteLeague(self.driver).maodian()
        sleep(2)

        #点击提交
        writeleague_page.WriteLeague(self.driver).Submit()
        sleep(1)

        #审核签约
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

            #进入加盟详情页
            po.LeagueDetails()
            sleep(2)

            # 点击通过
            po.Pass()
            sleep(1)

            #点击下拉框
            po.SiteAlert()
            sleep(3)
            #分配站点（一定要注意数据的准确性）
            #测试环境：①北京昌平站：1
            #          ②五家渠站点：38
            #          ③上海站点：2
            #线上环境：五家渠站点（12）：3
            po.selectsite("3")
            sleep(2)

            #确认
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

        #进入合同详情页
        leaguelist_page.LeagueList(self.driver).EidtContract()
        sleep(2)

        #点击编辑按钮
        contract_page.Contract(self.driver).Edit()
        sleep(2)

        #输入合同编号
        contract_page.Contract(self.driver).ContractID()
        sleep(2)

        #点击上传图片按钮
        contract_page.Contract(self.driver).ContractPhoto()
        sleep(2)

        #调用AutoIt完成上传图片
        os.system("D:/python/youjia/data/up.exe")
        sleep(1)

        #乙方姓名
        contract_page.Contract(self.driver).FirstParty()
        sleep(2)

        #乙方身份证
        contract_page.Contract(self.driver).IDcard()
        sleep(2)

        #选择权属（租赁）期限——开始时间
        contract_page.Contract(self.driver).ServiceDataStart()
        sleep(1)

        #选择权属（租赁）期限——结束时间
        contract_page.Contract(self.driver).ServiceDataEnd()
        sleep(2)

        #选择预计交房时间
        contract_page.Contract(self.driver).RoomTime()
        sleep(2)
        contract_page.Contract(self.driver).SelectDate()
        sleep(1)

        # 选择预计上线时间
        contract_page.Contract(self.driver).OnlineDate()
        sleep(2)
        contract_page.Contract(self.driver).SelectOnlineDate()
        sleep(2)

        #进入软装合同
        contract_page.Contract(self.driver).SoftContract()
        sleep(1)

        #输入运营升级费用
        contract_page.Contract(self.driver).OperationUpgradeFee(10)
        sleep(1)

        #输入软装费用
        contract_page.Contract(self.driver).SoftPic()
        sleep(1)

        #床垫选择购买
        contract_page.Contract(self.driver).BedBuy()
        sleep(1)

        #输入床垫费用
        contract_page.Contract(self.driver).BedFee(10)
        sleep(1)

        #选择有家银行卡
        contract_page.Contract(self.driver).Card()
        sleep(1)

        #输入品牌升级相关费用
        contract_page.Contract(self.driver).UpgradeCost()
        sleep(1)

        #点击上传图片按钮并上传
        contract_page.Contract(self.driver).SoftContractUp()
        sleep(2)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)

        #点击提交审核
        contract_page.Contract(self.driver).SubmissionOfAudit()
        sleep(2)
        contract_page.Contract(self.driver).ConfirmBtn()
        sleep(2)

        #审核通过
        contract_page.Contract(self.driver).Pass()
        sleep(2)
        contract_page.Contract(self.driver).AlertPass()
        sleep(2)

        # 确认收款
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

        #预约交接
        housemanagelist_page.HouseManagePage(self.driver).Appointment()
        sleep(1)

        #请录入与业主预约的交接时间——弹出时间插件
        housemanagelist_page.HouseManagePage(self.driver).AppointmentDate()
        sleep(1)
        #点击此刻
        housemanagelist_page.HouseManagePage(self.driver).ThisMoment()
        sleep(1)

        #确认按钮
        housemanagelist_page.HouseManagePage(self.driver).Determine()
        sleep(1)

        #点击完成交接
        housemanagelist_page.HouseManagePage(self.driver).CompleteAppointment()
        sleep(1)

        #上传图片
        housemanagelist_page.HouseManagePage(self.driver).AppointmentPicture()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(1)

        #预计筹建完成日——弹出时间控件
        housemanagelist_page.HouseManagePage(self.driver).CompletionDate()
        sleep(1)
        #点击此刻
        housemanagelist_page.HouseManagePage(self.driver).CompletionDateNow()
        sleep(1)

        #点击保存按钮
        housemanagelist_page.HouseManagePage(self.driver).AppointmentSave()
        sleep(1)

        housemanagelist_page.HouseManagePage(self.driver).wujiaqu()
        sleep(1)

        #点击完成验收
        housemanagelist_page.HouseManagePage(self.driver).CompletionOfAcceptance()
        sleep(1)

        #点击保存
        housemanagelist_page.HouseManagePage(self.driver).CompletionOfAcceptanceSave()
        sleep(1)

        #弹窗点击编辑房屋，进入房屋详情页
        housemanagelist_page.HouseManagePage(self.driver).AlertEditHouse()
        sleep(2)

        #编辑房屋
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
        housemanagelist_page.HouseManagePage(self.driver).Shower(2)
        sleep(1)

        # 床的数量
        housemanagelist_page.HouseManagePage(self.driver).SingleBed(2)
        sleep(1)

        # 上传封面照片
        housemanagelist_page.HouseManagePage(self.driver).Cover()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)

        #上传客厅照片
        housemanagelist_page.HouseManagePage(self.driver).Parlour()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)

        #上传卧室图片
        housemanagelist_page.HouseManagePage(self.driver).Bedroom()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)

        #上传厨房图片
        housemanagelist_page.HouseManagePage(self.driver).Kitchen()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)

        #上传卫浴照片
        housemanagelist_page.HouseManagePage(self.driver).Bathroom()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)

        #上传其他照片
        housemanagelist_page.HouseManagePage(self.driver).Other()
        sleep(1)
        os.system("D:/python/youjia/data/up.exe")
        sleep(2)

        #点击提交
        housemanagelist_page.HouseManagePage(self.driver).submitBtn()
        sleep(1)

        #获取房源ID
        housemanagelist_page.HouseManagePage(self.driver).wujiaqu()
        sleep(1)
        id = housemanagelist_page.HouseManagePage(self.driver).get_RoomID()
        sleep(1)

        #编辑房源
        nav_page.NavPage(self.driver).RoomManageList()
        sleep(0.5)

        #查询条件——输入房源id
        roommanagelist_page.RoomManageListPage(self.driver).SelectID(id)
        sleep(1)
        roommanagelist_page.RoomManageListPage(self.driver).wujiaqu()
        sleep(0.5)
        if roommanagelist_page.RoomManageListPage(self.driver).RoomState() == "待补充":

            #进入房源详情页
            roommanagelist_page.RoomManageListPage(self.driver).RoomId()
            sleep(1)

            #点击编辑按钮
            roommanagelist_page.RoomManageListPage(self.driver).Eidt()
            sleep(0.5)

            #输入房源简介
            roommanagelist_page.RoomManageListPage(self.driver).RoomIntroduce("测试测试测试")
            sleep(0.5)

            #输入日价
            roommanagelist_page.RoomManageListPage(self.driver).FloorPrice(60)
            sleep(0.5)

            #不设置周末价
            roommanagelist_page.RoomManageListPage(self.driver).NoSetUp()
            sleep(0.5)

            #输入押金
            roommanagelist_page.RoomManageListPage(self.driver).yajin(1)
            sleep(0.5)

            """
            默认都是选择1。
            1：不支持退款 2：宽松 
            PS：Airbnb 1对应的是宽松
           """
            roommanagelist_page.RoomManageListPage(self.driver).SelectRefund("1")
            sleep(0.5)

            """SelectRefundChannel()选择渠道1：蚂蚁 2：有家 3：途家 4：Airbnb"""
            roommanagelist_page.RoomManageListPage(self.driver).SelectRefundChannel("2")
            sleep(0.5)
            roommanagelist_page.RoomManageListPage(self.driver).SelectRefund()
            sleep(0.5)
            roommanagelist_page.RoomManageListPage(self.driver).SelectRefundChannel("3")
            sleep(0.5)
            roommanagelist_page.RoomManageListPage(self.driver).SelectRefund()
            sleep(0.5)
            roommanagelist_page.RoomManageListPage(self.driver).SelectRefundChannel("4")
            sleep(0.5)
            roommanagelist_page.RoomManageListPage(self.driver).SelectRefund()
            sleep(0.5)

            #入住人数
            roommanagelist_page.RoomManageListPage(self.driver).pople(4)
            sleep(0.5)

            #输入其他须知
            roommanagelist_page.RoomManageListPage(self.driver).Other("测试ceshi测试ceshi")
            sleep(0.5)

            #点击提交
            roommanagelist_page.RoomManageListPage(self.driver).Submit()
            sleep(1)

        #进入房源并审核通过
        roommanagelist_page.RoomManageListPage(self.driver).SelectID(id)
        sleep(0.5)
        roommanagelist_page.RoomManageListPage(self.driver).wujiaqu()
        sleep(1)
        roommanagelist_page.RoomManageListPage(self.driver).RoomId()
        sleep(1)
        roommanagelist_page.RoomManageListPage(self.driver).Pass()
        sleep(0.5)
        roommanagelist_page.RoomManageListPage(self.driver).TwoPass()
        sleep(0.5)

        #判断房源状态是否改为上线
        roommanagelist_page.RoomManageListPage(self.driver).SelectID(id)
        sleep(0.5)
        roommanagelist_page.RoomManageListPage(self.driver).wujiaqu()
        sleep(0.5)
        assert roommanagelist_page.RoomManageListPage(self.driver).RoomState() == "已上线"



if __name__ == "__main__":
    unittest.main()
