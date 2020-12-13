
class Task:
  def __init__(self, id, p_title, good, good_pictures, p_destination, d_destination, money, deadline, details, status, phone, author, time, puchaser=None, p_location=None, p_finish_time=None, p_send_location=None, p_details=None, p_money=None, deliver=None, d_current_location=None, d_finish_time=None, d_money=None, appraise=None, p_appraise=None, d_appraise=None):
    self.id = id
    self.p_title = p_title
    self.good = good
    self.good_pictures = good_pictures
    self.p_destination = p_destination # 带坐标
    self.d_destination = d_destination # 带坐标
    self.money = money
    self.deadline = deadline
    self.details = details
    self.status = status
    self.phone = phone
    self.author = author
    self.time = time
    
    # status == 1:
    self.puchaser = puchaser
    self.p_location = p_location
    self.p_finish_time = p_finish_time
    self.p_send_location = p_send_location
    self.p_details = p_details
    self.p_money = p_money

    # status == 2:
    self.deliver = deliver
    self.d_current_location = d_current_location
    self.d_finish_time = d_finish_time
    self.d_money = d_money

    # status == 3:
    self.appraise = appraise
    self.p_appraise = p_appraise
    self.d_appraise = d_appraise
    
