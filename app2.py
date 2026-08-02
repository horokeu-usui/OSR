import random
import streamlit as st

object_dic = {"center_cherry":1, "strong_cherry":50, "chance_com":110 , "tiny_cherry":171, "suika":217, "OSR_right":150, "OSR_center":1343, "OSR_left":1743, "OSR_straight":15, "OSR_fake":3277, "normal_rep":331, "bell_A":341, "bell_B":570, "bell_navi":8065}
buddy_dic = {"yoh":703, "yoh_ren":250, "yoh_ren_choco":23, "yoh_ren_choco_horo":16, "all":4}

def first_buddy_decision():
    bud = [1,0,0,0,0]
    bud_result = random.randint(1,996)
    if bud_result >= 704 and bud_result <= 953:
        dubble = random.randint(1,4)
        if dubble == 1:
            bud[1] = 1
        elif dubble == 2:
            bud[2] = 1
        elif dubble == 3:
            bud[3] = 1
        elif dubble == 4:
            bud[4] = 1
    elif bud_result >= 954 and bud_result <= 976:
        triple = random.randint(1,6)
        if triple == 1:
            bud[1] = 1
            bud[2] = 1
        elif triple == 2:
            bud[1] = 1
            bud[3] = 1
        elif triple == 3:
            bud[1] = 1
            bud[4] = 1
        elif triple == 4:
            bud[2] = 1
            bud[3] = 1
        elif triple == 5:
            bud[2] = 1
            bud[4] = 1
        elif triple == 6:
            bud[3] = 1
            bud[4] = 1
    elif bud_result >= 977 and bud_result <= 992:
        quatro = random.randint(1,4)
        if quatro == 1:
            bud[1] = 1
            bud[2] = 1
            bud[3] = 1
        elif quatro == 2:
            bud[1] = 1
            bud[2] = 1
            bud[4] = 1
        elif quatro == 3:
            bud[1] = 1
            bud[3] = 1
            bud[4] = 1
        elif quatro == 4:
            bud[2] = 1
            bud[3] = 1
            bud[4] = 1
    elif bud_result >= 993 and bud_result <= 996:
        bud[1] = 1
        bud[2] = 1
        bud[3] = 1
        bud[4] = 1
    return bud

#仲間参戦抽選。リセットした際に、現在の仲間、前Gのリセット有無を参照して、仲間の参戦抽選をする。
def buddy_add_rottely(reset_check,yoh,ren,choco,horo,rize):
    if yoh == 1 and ren == 0 and choco == 0 and horo == 0 and rize == 0:
        bud_add_result = [1,0,0,0,0]
        if reset_check == 1:
            add_reset_1 = random.randint(1,2)
            if add_reset_1 == 1:
                who4 = random.randint(1,4)
                if who4 == 1:
                    bud_add_result[1] = 1
                elif who4 == 2:
                    bud_add_result[2] = 1
                elif who4 == 3:
                    bud_add_result[3] = 1
                elif who4 == 4:
                    bud_add_result[4] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_1 = random.randint(1,1000)
            if add_non_reset_1 >= 1 and add_non_reset_1 <= 31:
                who4 = random.randint(1,4)
                if who4 == 1:
                    bud_add_result[1] = 1
                elif who4 == 2:
                    bud_add_result[2] = 1
                elif who4 == 3:
                    bud_add_result[3] = 1
                elif who4 == 4:
                    bud_add_result[4] = 1
            else:
                pass
    elif yoh == 1 and ren == 1 and choco == 0 and horo == 0 and rize == 0:
        bud_add_result = [1,1,0,0,0]
        if reset_check == 1:
            add_reset_2 = random.randint(1,1000)
            if add_reset_2 >= 1 and add_reset_2 <= 375:
                who3 = random.randint(1,3)
                if who3 == 1:
                    bud_add_result[2] = 1
                elif who3 == 2:
                    bud_add_result[3] = 1
                elif who3 == 3:
                    bud_add_result[4] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_2 = random.randint(1,1000)
            if add_non_reset_2 >= 1 and add_non_reset_2 <= 23:
                who3 = random.randint(1,3)
                if who3 == 1:
                    bud_add_result[2] = 1
                elif who3 == 2:
                    bud_add_result[3] = 1
                elif who3 == 3:
                    bud_add_result[4] = 1
            else:
                pass
    elif yoh == 1 and ren ==0 and choco == 1 and horo == 0 and rize == 0:
        bud_add_result = [1,0,1,0,0]
        if reset_check == 1:
            add_reset_2 = random.randint(1,1000)
            if add_reset_2 >= 1 and add_reset_2 <= 375:
                who3 = random.randint(1,3)
                if who3 == 1:
                    bud_add_result[1] = 1
                elif who3 == 2:
                    bud_add_result[3] = 1
                elif who3 == 3:
                    bud_add_result[4] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_2 = random.randint(1,1000)
            if add_non_reset_2 >= 1 and add_non_reset_2 <= 23:
                who3 = random.randint(1,3)
                if who3 == 1:
                    bud_add_result[1] = 1
                elif who3 == 2:
                    bud_add_result[3] = 1
                elif who3 == 3:
                    bud_add_result[4] = 1
            else:
                pass
    elif yoh == 1 and ren ==0 and choco == 0 and horo == 1 and rize == 0:
        bud_add_result = [1,0,0,1,0]
        if reset_check == 1:
            add_reset_2 = random.randint(1,1000)
            if add_reset_2 >= 1 and add_reset_2 <= 375:
                who3 = random.randint(1,3)
                if who3 == 1:
                    bud_add_result[1] = 1
                elif who3 == 2:
                    bud_add_result[2] = 1
                elif who3 == 3:
                    bud_add_result[4] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_2 = random.randint(1,1000)
            if add_non_reset_2 >= 1 and add_non_reset_2 <= 23:
                who3 = random.randint(1,3)
                if who3 == 1:
                    bud_add_result[1] = 1
                elif who3 == 2:
                    bud_add_result[2] = 1
                elif who3 == 3:
                    bud_add_result[4] = 1
            else:
                pass
    elif yoh == 1 and ren ==0 and choco == 0 and horo == 0 and rize == 1:
        bud_add_result = [1,0,0,0,1]
        if reset_check == 1:
            add_reset_2 = random.randint(1,1000)
            if add_reset_2 >= 1 and add_reset_2 <= 375:
                who3 = random.randint(1,3)
                if who3 == 1:
                    bud_add_result[1] = 1
                elif who3 == 2:
                    bud_add_result[2] = 1
                elif who3 == 3:
                    bud_add_result[3] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_2 = random.randint(1,1000)
            if add_non_reset_2 >= 1 and add_non_reset_2 <= 23:
                who3 = random.randint(1,3)
                if who3 == 1:
                    bud_add_result[1] = 1
                elif who3 == 2:
                    bud_add_result[2] = 1
                elif who3 == 3:
                    bud_add_result[3] = 1
            else:
                pass
    elif yoh == 1 and ren ==1 and choco == 1 and horo == 0 and rize == 0:
        bud_add_result = [1,1,1,0,0]
        if reset_check == 1:
            add_reset_3 = random.randint(1,1000)
            if add_reset_3 >= 1 and add_reset_3 <= 250:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[3] = 1
                elif who2 == 2:
                    bud_add_result[4] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_3 = random.randint(1,1000)
            if add_non_reset_3 >= 1 and add_non_reset_3 <= 16:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[3] = 1
                elif who2 == 2:
                    bud_add_result[4] = 1
            else:
                pass
    elif yoh == 1 and ren ==1 and choco == 0 and horo == 1 and rize == 0:
        bud_add_result = [1,1,0,1,0]
        if reset_check == 1:
            add_reset_3 = random.randint(1,1000)
            if add_reset_3 >= 1 and add_reset_3 <= 250:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[2] = 1
                elif who2 == 2:
                    bud_add_result[4] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_3 = random.randint(1,1000)
            if add_non_reset_3 >= 1 and add_non_reset_3 <= 16:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[2] = 1
                elif who2 == 2:
                    bud_add_result[4] = 1
            else:
                pass
    elif yoh == 1 and ren ==1 and choco == 0 and horo == 0 and rize == 1:
        bud_add_result = [1,1,0,0,1]
        if reset_check == 1:
            add_reset_3 = random.randint(1,1000)
            if add_reset_3 >= 1 and add_reset_3 <= 250:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[2] = 1
                elif who2 == 2:
                    bud_add_result[3] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_3 = random.randint(1,1000)
            if add_non_reset_3 >= 1 and add_non_reset_3 <= 16:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[2] = 1
                elif who2 == 2:
                    bud_add_result[3] = 1
            else:
                pass
    elif yoh == 1 and ren ==0 and choco == 1 and horo == 1 and rize == 0:
        bud_add_result = [1,0,1,1,0]
        if reset_check == 1:
            add_reset_3 = random.randint(1,1000)
            if add_reset_3 >= 1 and add_reset_3 <= 250:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[1] = 1
                elif who2 == 2:
                    bud_add_result[4] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_3 = random.randint(1,1000)
            if add_non_reset_3 >= 1 and add_non_reset_3 <= 16:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[1] = 1
                elif who2 == 2:
                    bud_add_result[4] = 1
            else:
                pass
    elif yoh == 1 and ren ==0 and choco == 1 and horo == 0 and rize == 1:
        bud_add_result = [1,0,1,0,1]
        if reset_check == 1:
            add_reset_3 = random.randint(1,1000)
            if add_reset_3 >= 1 and add_reset_3 <= 250:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[1] = 1
                elif who2 == 2:
                    bud_add_result[3] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_3 = random.randint(1,1000)
            if add_non_reset_3 >= 1 and add_non_reset_3 <= 16:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[1] = 1
                elif who2 == 2:
                    bud_add_result[3] = 1
            else:
                pass
    elif yoh == 1 and ren ==0 and choco == 0 and horo == 1 and rize == 1:
        bud_add_result = [1,0,0,1,1]
        if reset_check == 1:
            add_reset_3 = random.randint(1,1000)
            if add_reset_3 >= 1 and add_reset_3 <= 250:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[3] = 1
                elif who2 == 2:
                    bud_add_result[4] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_3 = random.randint(1,1000)
            if add_non_reset_3 >= 1 and add_non_reset_3 <= 16:
                who2 = random.randint(1,2)
                if who2 == 1:
                    bud_add_result[3] = 1
                elif who2 == 2:
                    bud_add_result[4] = 1
            else:
                pass
    elif yoh == 1 and ren ==1 and choco == 1 and horo == 1 and rize == 0:
        bud_add_result = [1,1,1,1,0]
        if reset_check == 1:
            add_reset_4 = random.randint(1,1000)
            if add_reset_4 >= 1 and add_reset_4 <= 125:
                bud_add_result[4] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_4 = random.randint(1,1000)
            if add_non_reset_4 >= 1 and add_non_reset_4 <= 8:
                bud_add_result[4] = 1
            else:
                pass
    elif yoh == 1 and ren ==1 and choco == 1 and horo == 0 and rize == 1:
        bud_add_result = [1,1,1,0,1]
        if reset_check == 1:
            add_reset_4 = random.randint(1,1000)
            if add_reset_4 >= 1 and add_reset_4 <= 125:
                bud_add_result[3] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_4 = random.randint(1,1000)
            if add_non_reset_4 >= 1 and add_non_reset_4 <= 8:
                bud_add_result[3] = 1
            else:
                pass
    elif yoh == 1 and ren ==1 and choco == 0 and horo == 1 and rize == 1:
        bud_add_result = [1,1,0,1,1]
        if reset_check == 1:
            add_reset_4 = random.randint(1,1000)
            if add_reset_4 >= 1 and add_reset_4 <= 125:
                bud_add_result[2] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_4 = random.randint(1,1000)
            if add_non_reset_4 >= 1 and add_non_reset_4 <= 8:
                bud_add_result[2] = 1
            else:
                pass
    elif yoh == 1 and ren ==0 and choco == 1 and horo == 1 and rize == 1:
        bud_add_result = [1,0,1,1,1]
        if reset_check == 1:
            add_reset_4 = random.randint(1,1000)
            if add_reset_4 >= 1 and add_reset_4 <= 125:
                bud_add_result[1] = 1
            else:
                pass
        elif reset_check == 0:
            add_non_reset_4 = random.randint(1,1000)
            if add_non_reset_4 >= 1 and add_non_reset_4 <= 8:
                bud_add_result[1] = 1
            else:
                pass
    return bud_add_result

def object_decision():
    result = random.randint(1,16384)
    if result == 1:
        obj = "center_cherry"
    elif result >= 2 and result <= 51:
        obj = "strong_cherry"
    elif result >= 52 and result <= 161:
        obj = "chance_com"
    elif result >= 162 and result <= 332:
        obj = "tiny_cherry"
    elif result >= 333 and result <= 549:
        obj = "suika"
    elif result >= 550 and result <= 699:
        obj = "OSR_right"
    elif result >= 700 and result <= 2042:
        obj = "OSR_center"
    elif result >= 2043 and result <= 3792:
        obj = "OSR_left"
    elif result >= 3793 and result <= 3807:
        obj = "OSR_straight"
    elif result >= 3808 and result <= 7084:
        obj = "OSR_fake"
    elif result >= 7085 and result <= 7415:
        obj = "normal_rep"
    elif result >= 7416 and result <= 7757:
        obj = "bell_A"
    elif result >= 7758 and result <= 8328:
        obj = "bell_B"
    elif result >= 8329 and result <= 16384:
        obj = "bell_navi"
    return obj

def addition_table_decision(obj,bud,bell_navi_count):
    if obj == "center_cherry":
            table = 6
    elif obj == "strong_cherry":
        if bud[4] == 1:
            if  random.randint(1,4) == 1:
                 table = 6
            else:
                 table = 5
        elif bud[4] == 0:
             table = 4
    elif obj == "chance_com":
        if bud[4] == 1:
             if random.randint(1,1000) <= 63:
                 table = 6
             else:
                  table =5
        elif bud[4] == 0:
             table = 3
    elif obj == "tiny_cherry":
        if bud[4] == 1:
             table = 4
        elif bud[4] == 0:
             table = 2
    elif obj == "suika":
        if bud[4] == 1:
             table = 5
        elif bud[4] == 0:
             table = 3
    elif obj == "OSR_right":
        if bud[1] == 1:
            if random.randint(1,1000) <= 102:
                  table = 2
            else:
                 table = 1
        elif bud[1] == 0:
                 table = 0
    elif obj == "OSR_center":
        if bud[1] == 1:
            if random.randint(1,1000) <= 102:
                  table = 2
            else:
                 table = 1
        elif bud[1] == 0:
             table = 0
    elif obj == "OSR_left":
        if bud[1] == 1:
            if random.randint(1,1000) <= 102:
                table = 2
            else:
                table = 1
        elif bud[1] == 0:
             table = 0
    elif obj == "OSR_straight":
        if bud[1] == 1:
            table = 6
        elif bud[1] == 0:
            table = 5
    elif obj == "OSR_fake":
        if bud [3] == 1:
            if random.randint(1,2) == 1:
                table = 2
            else:
                table = 0
        elif bud[3] == 0:
             table = 0
    elif obj == "normal_rep":
        if bud[3] == 1:
             if random.randint(1,4) == 1:
                  table = 3
             else:
                  table = 2
        elif bud[3] == 0:
            if random.randint(1,1000) <= 31:
                table = 2
            else:
                table = 1
    elif obj == "bell_A" or obj == "bell_B":
        if bell_navi_count == 0:
            table = 2
        elif bell_navi_count == 1:
            if bud[2] == 1:
                table = 1
            elif bud[2] ==0:
                if random.randint(1,2) == 1:
                    table = 0
                else:
                    table = 1
    elif obj == "bell_navi":
        if bell_navi_count == 0:
            table = 2
        elif bell_navi_count == 1:
            if bud[2] == 1:
                table = 1
            elif bud[2] ==0:
                if random.randint(1,2) == 1:
                    table = 0
                else:
                    table = 1
    return table

def addition_game_decision(tab):
    add_game = 0
    if tab == 0:
        add_game += 0
    elif tab == 1:
        tab1 = random.randint(1,1000)
        if tab1 >= 1 and tab1 <= 957:
            add_game += 5
        elif tab1 >= 958 and tab1 <= 996:
            add_game += 10
        elif tab1 >= 997 and tab1 <= 10000:
            add_game += 20
    elif tab == 2:
        tab2 = random.randint(1,1000)
        if tab2 >= 1 and tab2 <= 972:
            add_game += 10
        elif tab2 >= 973 and tab2 <= 988:
            add_game += 20
        elif tab2 >= 989 and tab2 <= 996:
            add_game += 30
        elif tab2 >= 997 and tab2 <= 1000:
            add_game += 50
    elif tab == 3:
        tab3 = random.randint(1,1000)
        if tab3 >= 1 and tab3 <= 957:
            add_game += 20
        elif tab3 >= 958 and tab3 <= 988:
            add_game += 30
        elif tab3 >= 989 and tab3 <= 996:
            add_game += 50
        elif tab3 >= 997 and tab3 <= 1000:
            add_game += 100
    elif tab == 4:
        tab4 = random.randint(1,1000)
        if tab4 >= 1 and tab4 <= 965:
            add_game += 30
        elif tab4 >= 966 and tab4 <= 996:
            add_game += 50
        elif tab4 >= 997 and tab4 <= 1000:
            add_game += 100
    elif tab == 5:
        tab5 = random.randint(1,1000)
        if tab5 >= 1 and tab5 <= 953:
            add_game += 50
        elif tab5 >= 954 and tab5 <= 992:
            add_game += 100
        elif tab5 >= 993 and tab5 <= 996:
            add_game += 200
        elif tab5 >= 997 and tab5 <= 1000:
            add_game += 300
    elif tab == 6:
        tab6 = random.randint(1,1000)
        if tab6 >= 1 and tab6 <= 922:
            add_game += 100
        elif tab6 >= 923 and tab6 <= 969:
            add_game += 200
        elif tab6 >= 970 and tab6 <= 1000:
            add_game += 300
    return add_game


def run_simulation():
    """
    元のwhileループの処理をそのまま関数化したもの。
    printしていた内容を、1ゲームごとの辞書としてlistにためて返す。
    """
    log = []

    bud0 = ""
    bud1 = ""
    bud2 = ""
    bud3 = ""
    bud4 = ""
    addition_table = 0
    addition_game = 0
    total_game = 0
    last_game = 5
    bell_navi_count = 0
    previous_reset_check = 1

    buddy = first_buddy_decision()

    while last_game != 0:
        obj = object_decision()
        addition_table = addition_table_decision(obj, buddy, bell_navi_count)
        addition_game = addition_game_decision(addition_table)
        total_game += addition_game

        if obj in ("center_cherry", "strong_cherry", "chance_com", "tiny_cherry",
                   "suika", "OSR_right", "OSR_center", "OSR_left", "OSR_straight"):
            last_game = 5
            previous_reset_check = 1
            buddy = buddy_add_rottely(previous_reset_check, buddy[0], buddy[1], buddy[2], buddy[3], buddy[4])
        elif obj in ("OSR_fake", "normal_rep", "bell_A", "bell_B", "bell_navi"):
            last_game -= 1
            previous_reset_check = 0
            if obj == "bell_navi":
                bell_navi_count = 1

        if last_game == 0 and total_game == 0:
            last_game = 5

        if buddy[0] == 1:
            bud0 = "葉"
        if buddy[1] == 1:
            bud1 = ",蓮"
        if buddy[2] == 1:
            bud2 = ",チョコ"
        if buddy[3] == 1:
            bud3 = ",ホロ"
        if buddy[4] == 1:
            bud4 = ",リゼ"

        log.append({
            "仲間": bud0 + bud1 + bud2 + bud3 + bud4,
            "引いた小役": obj,
            "上乗せテーブル": addition_table,
            "上乗せG数": addition_game,
            "トータルG数": total_game,
            "残りG数": last_game,
        })

    return log


# ----------------- ここからStreamlit画面 -----------------

st.set_page_config(page_title="OSRミュレーター", page_icon="🎰")
st.title("🎰 OSRミュレーター")
st.write("ボタンを押すと、1回分の抽選結果が表示されます。")

if st.button("開始", type="primary"):
    result_log = run_simulation()
    st.success(f"最終トータルG数：{result_log[-1]['トータルG数']} G")
    for i, row in enumerate(result_log, start=1):
        st.markdown(f"**--- {i}ゲーム目 ---**")
        st.write(f"【仲間】→ {row['仲間']}")
        st.write(f"【引いた小役】→ {row['引いた小役']}")
        st.write(f"【上乗せテーブル】→ {row['上乗せテーブル']}")
        st.write(f"【上乗せG数】→ {row['上乗せG数']}")
        st.write(f"【トータルG数】→ {row['トータルG数']}")
        st.write(f"【残りG数】→ {row['残りG数']}")
        st.divider()
