const switching = document.getElementById('switch');

if(switching){
    switching.addEventListener('change', () =>{
        document.body.classList.toggle('dark')
    })
}
