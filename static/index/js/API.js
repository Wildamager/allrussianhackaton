
async function getResult(){
    let result = await getAll();
    return result
}

async function doTask(){
    let data = await getResult();
    console.log(data.data)
    document.getElementById('number').innerHTML = data.data;

}

function getAll(){
    try {
        const response = axios.get(`http://127.0.0.1:8000/dashboard/stream/result`+`/`+window.location.pathname.split('/').reverse()[0]);
        const todoItems = response;
        console.log(`GET: Here's the list of todos`, todoItems);
    
        return todoItems;
      } catch (errors) {
        console.error(errors);
      }
}


