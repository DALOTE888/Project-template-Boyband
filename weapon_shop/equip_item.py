# =====================================================
#  weapon_shop/equip_item.py
# =====================================================

def equip_item(person, weapon):
    # เช็คเงิน
    if person["money"] < weapon["price"]:
        return {
            "status": False,
            "message": "เงินไม่พอ"
        }

    # เช็คว่ามีอาวุธอยู่แล้วหรือไม่
    if person["equipment"] != "ไม่มี":
        return {
            "status": False,
            "message": "มีอาวุธอยู่แล้ว"
        }

    # ซื้อและติดตั้งอาวุธ
    person["money"] -= weapon["price"]
    person["equipment"] = weapon["name"]
    person["power"] += weapon["bonus"]

    return {
        "status": True,
        "message": "ติดตั้งอาวุธสำเร็จ"
    }


# ทดสอบ: python -m weapon_shop.equip_item
if __name__ == "__main__":
    vito = {"name": "Vito", "money": 60000, "power": 5, "equipment": "ไม่มี"}
    gun = {"name": "ปืนพก 9mm", "price": 50000, "bonus": 5}

    print(equip_item(vito, gun))   # ต้องได้ status True
    print(vito)                    # เงินเหลือ 10000, power เป็น 10, equipment เป็นปืน
    print(equip_item(vito, gun))   # ครั้งที่สองต้องได้ status False