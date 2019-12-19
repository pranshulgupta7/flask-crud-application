function edit(id) {
    localStorage.setItem('id',id)
    let vali = localStorage.getItem('id')
    console.log(vali)
    document.getElementById('id').value = vali
}