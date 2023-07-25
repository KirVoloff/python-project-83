from flask import \
    render_template, \
    flash, \
    url_for, redirect, \
    get_flashed_messages
import page_analyzer.db as db


def handle_invalid_url(url):
    flash('Некорректный URL', 'alert-danger')
    messages = get_flashed_messages(with_categories=True)
    return render_template('index.html', url=url, messages=messages), 422


def handle_existing_url(url):
    flash('Страница уже существует', 'alert-info')
    return redirect(url_for('url_get', id=db.find_url(url).id))


def handle_error(url):
    flash('Произошла ошибка', 'alert-danger')
    messages = get_flashed_messages(with_categories=True)
    return render_template('index.html', url=url, messages=messages), 500


def handle_success(result):
    flash('Страница успешно добавлена', 'alert-success')
    return redirect(url_for('url_get', id=result))
