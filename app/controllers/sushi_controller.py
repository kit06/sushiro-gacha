from flask import Blueprint, redirect, render_template, request
from ..models.models import Db

sushi_controller_bp = Blueprint('sushi_controller', __name__)

@sushi_controller_bp.route('/')
def gacha():
    return redirect('/sushi-gacha')

@sushi_controller_bp.route('/sushi-gacha', methods=['GET', 'POST'])
def submit_result():
    if request.method == 'POST':
        budget = int(request.form.get('budget'))
        # ガチャの結果を生成する処理
        result, total_price = generate_gacha_result(budget)
        # 結果を画面に返す
        return render_template('result.html', result=result, total_price=total_price,budget=budget)
    else:
        return render_template('sushi-gacha.html')

def generate_gacha_result(budget):
    db = Db()
    # 最低価格の取得
    min_price = db.calc_min_price()
    # 合計価格と結果の宣言
    total_price = 0
    result = []
    # 予算 - 現在のガチャ結果の合計金額が最低価格を下回るまでループ
    while budget - total_price >= min_price:
        sushi = db.get_random_sushi_data_within_budget(budget - total_price)
        result.append(sushi)
        total_price += sushi.price
    return result, total_price
