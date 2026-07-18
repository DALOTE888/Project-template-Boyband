# =====================================================
#  personnel/search_member.py — คนรับผิดชอบ: ____________อันดาน่ารัก________
# =====================================================
from data import family_members

# TODO: สร้างฟังก์ชัน search_member(target_name)
#   - หาคนใน family_members ที่ชื่อตรงกับ target_name (ไม่สนตัวพิมพ์ใหญ่/เล็ก)
#   - เจอ -> return dict ของคนนั้น | ไม่เจอ -> return None
def search_member(name):
    for member in family_members:
        if member["name"].lower() == name.lower():
            return member
    return None
# ทดสอบ: python -m personnel.search_member
if __name__ == "__main__":
    print(search_member("tony").lower())        # ต้องได้ dict ของ Tony (พิมพ์เล็กก็ต้องเจอ)
    print(search_member("ไม่มีคนนี้"))    # ต้องได้ None


