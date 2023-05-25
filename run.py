from flask import Flask, request, redirect, render_template, flash
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
