let vc = "https://ntvyl8vvpe.execute-api.us-west-1.amazonaws.com/Prod/counter"

updateVisitCount();

function updateVisitCount() {
    fetch(vc)
        .then(response => response.json()
          .then(data => {
              document.getElementById('count').innerHTML = data;
          })
        )
}