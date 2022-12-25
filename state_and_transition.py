

#   father's family
state_fathers_family = ["爸爸的親戚(含)","父親的父母", "父親的兄弟姊妹", "父親的姪男/女、甥男/女"]#, "父親的祖父母、外祖父母"]
                        #["父親", "祖父/祖母（爺爺/奶奶）", "叔父(叔母)/伯父(伯母)", "姑姑(姑父)", "堂兄弟姊妹", "(姑)表兄弟姊妹",
                        #"曾祖父/曾祖母", "曾外祖父/曾外祖母", "兄弟姐妹", "姪男/女 or 甥男/女", "祖父母 or 外祖父母"]
transition_fathers_family = [
        {"trigger": "advance","source": "relation","dest": "爸爸的親戚(含)", "conditions": "is_going_fathers_family"},
        {"trigger": "advance","source": "爸爸的親戚(含)","dest": "父親的父母", "conditions": "is_going_f_parents"},
        {"trigger": "advance","source": "爸爸的親戚(含)","dest": "父親的兄弟姊妹", "conditions": "is_going_f_siblings"},
        {"trigger": "advance","source": "爸爸的親戚(含)","dest": "父親的姪男/女、甥男/女", "conditions": "is_going_f_nephews"},
        # {"trigger": "advance","source": "爸爸的親戚(含)","dest": "父親的祖父母、外祖父母"},
        
        {"trigger": "advance","source": ["父親的父母","父親的兄弟姊妹", "父親的姪男/女、甥男/女"],"dest": "dothings", "conditions": "is_going_dothings"},

]

#   mother's family
state_mothers_family = ["媽媽的親戚(含)", "母親的父母", "母親的兄弟姊妹", "母親的姪男/女、甥男/女"]#, "母親的祖父母、外祖父母"]
                        #["媽媽", "外祖父/外祖母（外公/外婆）", "舅父（舅母）", "姨母（姨父）", "(舅)表兄弟姊妹",
                        #"姨兄弟姊妹", "外曾祖父/外曾祖母","外曾外祖父/外曾外祖母"]
transition_mothers_family = [
    {"trigger": "advance","source": "relation","dest": "媽媽的親戚(含)", "conditions": "is_going_mothers_family"},
    {"trigger": "advance","source": "媽媽的親戚(含)","dest": "母親的父母", "conditions": "is_going_m_parents"},
    {"trigger": "advance","source": "媽媽的親戚(含)","dest": "母親的兄弟姊妹", "conditions": "is_going_m_siblings"},
    {"trigger": "advance","source": "媽媽的親戚(含)","dest": "母親的姪男/女、甥男/女", "conditions": "is_going_m_nephews"},
    # {"trigger": "advance","source": "媽媽的親戚(含)","dest": "母親的祖父母、外祖父母"},
    {"trigger": "advance","source": ["母親的父母","母親的兄弟姊妹", "母親的姪男/女、甥男/女"],"dest": "dothings", "conditions": "is_going_dothings"},
    
]

state_system = ["begin", "menu", "relation", "money", "income", "expense", "image", "document", "dothings", "earn", "speend"]

transition_system = [
    {"trigger": "advance","source": "begin","dest": "menu", "conditions": "is_going_menu"},
    {"trigger": "advance","source": "menu","dest": "relation", "conditions": "is_going_relation"},
    {"trigger": "advance","source": "menu","dest": "image", "conditions": "is_going_image"},
    {"trigger": "advance","source": "menu","dest": "money", "conditions": "is_going_money"},
    {"trigger": "advance","source": "menu","dest": "document", "conditions": "is_going_document"},
    {"trigger": "advance","source": "relation","dest": "menu", "conditions": "is_back_menu"},
    {"trigger": "advance","source": "money","dest": "menu", "conditions": "is_back_menu"},
    {"trigger": "advance","source": "image","dest": "menu", "conditions": "is_back_menu"},
    {"trigger": "advance","source": "document","dest": "menu", "conditions": "is_back_menu"},
    {"trigger": "advance","source": "image","dest": "image", "conditions": "more_image"},
    {"trigger": "advance","source": "dothings","dest": "menu", "conditions": "is_going_menu"},
    {"trigger": "advance","source": "dothings","dest": "earn", "conditions": "is_going_earn"},
    {"trigger": "advance","source": "dothings","dest": "speend", "conditions": "is_going_pay"},
    {"trigger": "advance","source": "dothings","dest": "image", "conditions": "is_going_image"},
    {"trigger": "advance","source": "earn","dest": "money", "conditions": "update_earn"},
    {"trigger": "advance","source": "speend","dest": "money", "conditions": "update_speend"},
    # {"trigger": "go_menu","source": "document","dest": "menu"},
    {"trigger": "advance","source": "money","dest": "income", "conditions": "is_going_income"},
    {"trigger": "advance","source": "money","dest": "expense", "conditions": "is_going_expense"},
    {"trigger": "advance","source": "money","dest": "menu", "conditions": "is_going_menu"},
    {"trigger": "advance","source": "income","dest": "money", "conditions": "is_going_money"},
    {"trigger": "advance","source": "expense","dest": "money", "conditions": "is_going_money"},
    {"trigger": "advance","source": "income","dest": "menu", "conditions": "is_going_menu"},
    {"trigger": "advance","source": "expense","dest": "menu", "conditions": "is_going_menu"},
    
  
]