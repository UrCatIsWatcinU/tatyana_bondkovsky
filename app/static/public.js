// этот файл будет исполнятся на любой странице, так как он включен в публичные скрипты в layout.html

// массив с задачами, которые необходимо выполнить, когда страница полностью загрузилась
const tasks = [];

const main = () => {
    const loading = document.querySelector('.loading');
    if(loading) loading.remove();
    document.body.classList.remove('while-loading'); 
    
    tasks.forEach(task => {
        if(typeof(task) == 'function'){
            try{
                task();
            }catch(err){
                showModal('Критическая ошибка', 'Пожалуйста, сообщите об этом администратору. Текст ошибки: ' + err)
            }
        }
    });
}

window.addEventListener('load', main);