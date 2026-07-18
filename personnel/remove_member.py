# =====================================================
#  personnel/remove_member.py — คนรับผิดชอบ: Boss
# =====================================================
from data import family_members

# TODO: สร้างฟังก์ชัน remove_member(target_name)
#   - หาคนที่ชื่อตรงกับ target_name (ไม่สนตัวพิมพ์ใหญ่/เล็ก) แล้วลบออกจาก family_members
#   - ลบสำเร็จ -> return True | ไม่เจอ -> return False


def remove_member(target_name):
    target_name = input("ชื่อลูกน้องที่อยากเก็บ: ").lower()


    for i in family_members:
        if target_name == i["name"].lower():
            family_members.remove(i)
            return "สั่งเก็บลูกน้องเรียบร้อยแล้ว"
        else:
           return "ไม่พบชื่อในระบบ"




# ทดสอบ: python -m personnel.remove_member
if __name__ == "__main__":
    print(remove_member("Luigi"))   # ครั้งแรกต้องได้ True
    print(remove_member("Luigi"))   # ครั้งที่สองต้องได้ False (ลบไปแล้ว)
    print(family_members)           # ต้องเหลือแค่ Tony
