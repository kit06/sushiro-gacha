# sushiro-gacha
This is Sushiro-gacha's apprication

```
sushiro-gacha/
├── app/
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── sushi_controller.py  # ルーティングとビューロジックを担当するコントローラー
│   ├── models/
│   │   ├── __init__.py
│   │   └── sushi.py  # データモデルとデータベースの操作を担当するモデル
│   ├── views/
│   │   ├── __init__.py
│   │   └── sushi_view.py  # ビューの表示を担当するビュー
│   └── __init__.py
├── config/
│   ├── __init__.py
│   └── database.py  # データベースの設定や接続情報を管理するファイル
├── migrations/
│   └── ...
├── static/
│   └── ...
├── templates/
│   └── ...
├── tests/
│   └── ...
├── .env  # 環境変数の設定ファイル
├── .gitignore
├── README.md
└── run.py  # アプリケーションのエントリーポイント
```

##各ファイルの簡単なサンプル

### app/controllers/sushi_controller.py:
```
from flask import render_template

from app.models.sushi import Sushi
from app import app

@app.route('/')
def gacha():
    sushi_list = Sushi.query.all()
    return render_template('home.html', sushi_list=sushi_list)

@app.route('/sushi/<int:sushi_id>')
def get_sushi(sushi_id):
    sushi = Sushi.query.get(sushi_id)
    return render_template('sushi.html', sushi=sushi)
```

### app/models/sushi.py:
```
from app import db

class Sushi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    calorie = db.Column(db.Integer, nullable=False)

    def __init__(self, name, category, price, calorie):
        self.name = name
        self.category = category
        self.price = price
        self.calorie = calorie
```

### app/templates/base.html:
```
<!DOCTYPE html>
<html>
<head>
    <title>My Sushi App</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
        </ul>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

### app/templates/home.html:
```
{% extends 'base.html' %}

{% block content %}
    <h1>Welcome to My Sushi App!</h1>
    <ul>
        {% for sushi in sushi_list %}
            <li>{{ sushi.name }} - {{ sushi.category }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

### app/templates/sushi.html:
```
{% extends 'base.html' %}

{% block content %}
    <h1>{{ sushi.name }}</h1>
    <p>Category: {{ sushi.category }}</p>
    <p>Price: {{ sushi.price }}</p>
    <p>Calories: {{ sushi.calorie }}</p>
{% endblock %}
```

### config/database.py:
```
from flask_sqlalchemy import SQLAlchemy

from app import app

# PostgreSQLへの接続情報を設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/myappdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemyのインスタンスを作成
db = SQLAlchemy(app)
このサンプルでは、ルートパス(/)へのリクエストでは全ての寿司情報を表示し、/sushi/<sushi_id>のようなURLへのリクエストでは指定された寿司の詳細情報を表示します。データベースへの接続情報はconfig/database.pyで設定され、app/models/sushi.pyではデータモデルが定義されています。ビューはapp/templates/ディレクトリ内のテンプレートファイルを使用して表示されます。
```

## 参考用 myapp/app/routes.py:
```
from flask import Blueprint, jsonify, request
from myapp.app.services.sushi_service import SushiService

# Create a Blueprint for the routes
sushi_bp = Blueprint('sushi', __name__)

# Instantiate the SushiService
sushi_service = SushiService()

# Define a route for getting sushi data
@sushi_bp.route('/sushi', methods=['GET'])
def get_sushi():
    sushi_data = sushi_service.get_all_sushi()
    return jsonify(sushi_data), 200

# Define a route for creating a new sushi
@sushi_bp.route('/sushi', methods=['POST'])
def create_sushi():
    sushi_info = request.get_json()
    created_sushi = sushi_service.create_sushi(sushi_info)
    return jsonify(created_sushi), 201

# Define a route for updating an existing sushi
@sushi_bp.route('/sushi/<int:sushi_id>', methods=['PUT'])
def update_sushi(sushi_id):
    sushi_info = request.get_json()
    updated_sushi = sushi_service.update_sushi(sushi_id, sushi_info)
    return jsonify(updated_sushi), 200

# Define a route for deleting a sushi
@sushi_bp.route('/sushi/<int:sushi_id>', methods=['DELETE'])
def delete_sushi(sushi_id):
    sushi_service.delete_sushi(sushi_id)
    return '', 204
```
