
class Task:
    def __init__(self, id, p_title, good, good_pictures, p_destination, d_destination, money, deadline, details, status, phone, author, time, puchaser=None, p_location=None, p_finish_time=None, p_send_location=None, p_details=None, p_money=None, deliver=None, d_current_location=None, d_finish_time=None, d_money=None, appraise=None, p_appraise=None, d_appraise=None, special_user=None):
        
        ##########################################################

        # status == 0: 待接受

        # 任务id
        self.id = id
        # 任务状态
        self.status = status
        # 专属任务对象
        self.special_user = special_user
        # 任务标题
        self.p_title = p_title
        # 货品名称
        self.good = good
        # 货品图像url数组，最多3张
        self.good_pictures = good_pictures
        # 配送目的地（采购人目的地），带坐标
        self.p_destination = p_destination
        # 期望采购地点，带坐标
        self.d_destination = d_destination
        # 期望总价
        self.money = money
        # 最晚取货时间
        self.deadline = deadline
        # 发布信息
        self.details = details
        # 发布人联系电话
        self.phone = phone
        # 发布人
        self.author = author
        # 发布时间戳
        self.time = time

        ##########################################################

        # status == 1: 采购中

        # 采购人
        self.puchaser = puchaser

        ##########################################################

        # status == 2: 待配送

        # 实际采购地点
        self.p_location = p_location
        # 采购完毕时间
        self.p_finish_time = p_finish_time
        # 寄送地点
        self.p_send_location = p_send_location
        # 采购信息
        self.p_details = p_details
        # 实际采购价格
        self.p_money = p_money

        ##########################################################

        # status == 3: 配送中

        # 配送者
        self.deliver = deliver
        # 配送者当前地点
        self.d_current_location = d_current_location
        
        ##########################################################

        # status == 4: 待付款

        # 配送完成时间
        self.d_finish_time = d_finish_time
        # 实际配送金额
        self.d_money = d_money

        ##########################################################

        # status == 5: 待评价

        ##########################################################

        # status == 6: 已结束

        # 总体评价
        self.appraise = appraise
        # 采购评价
        self.p_appraise = p_appraise
        # 配送评价
        self.d_appraise = d_appraise
