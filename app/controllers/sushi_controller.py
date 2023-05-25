from flask import Blueprint, redirect, render_template, request
from models import get_sushi_data

sushi_controller_bp = Blueprint('sushi_controller', __name__)

@sushi_controller_bp.route('/')
def gacha():
    return redirect('/gacha/sushi')

@sushi_controller_bp.route('/gacha/sushi', methods=['GET', 'POST'])
def submit_result():
    if request.method == 'POST':
        sushi = request.form.get('sushi')

        if sushi == '1':
            # ガチャの結果を生成する処理
            result = generate_gacha_result()

            # 結果を画面に返す
            return render_template('sushi-gacha.html', sushi=result)

    return render_template('sushi-gacha.html')

# TODO: ビジネスロジックの実装
def generate_gacha_result():
    sushi = get_sushi_data()
    # TODO: ガチャの処理
