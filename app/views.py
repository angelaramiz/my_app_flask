# app/views.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Task

main = Blueprint('main', __name__)

@main.route('/')
def home():
    # Obtener tareas agrupadas por estado
    tasks_pendiente = Task.query.filter_by(status='pendiente').all()
    tasks_en_proceso = Task.query.filter_by(status='en_proceso').all()
    tasks_finalizado = Task.query.filter_by(status='finalizado').all()
    
    return render_template('home.html', 
        tasks_pendiente=tasks_pendiente,
        tasks_en_proceso=tasks_en_proceso,
        tasks_finalizado=tasks_finalizado)

@main.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    
    if not title:
        flash('El título es obligatorio', 'danger')
        return redirect(url_for('main.home'))
    
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    flash('Tarea añadida con éxito', 'success')
    return redirect(url_for('main.home'))

@main.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    new_status = request.form.get('new_status')
    
    if new_status in ['pendiente', 'en_proceso', 'finalizado']:
        task.status = new_status
        db.session.commit()
        flash('Estado de tarea actualizado', 'success')
    
    return redirect(url_for('main.home'))

@main.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        db.session.commit()
        flash('Tarea actualizada con éxito', 'success')
        return redirect(url_for('main.home'))
    
    return render_template('edit_task.html', task=task)

@main.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Tarea eliminada con éxito', 'success')
    return redirect(url_for('main.home'))
