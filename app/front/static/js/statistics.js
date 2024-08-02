

// API REQUESTS


// get_completed_achievements_num

async function get_completed_achievements_num() {
  const completedAchievementsNumP = document.getElementById('completedAchievementsNum');


  let response = await fetch('/api/get_completed_achievements_num/' + window.location.href.split('/').pop());

  if (response.ok) { // если HTTP-статус в диапазоне 200-299
    // получаем тело ответа (см. про этот метод ниже)
    let data = await response.json();
    completedAchievementsNumP.innerText = data['num'];
  } else {
    alert("Ошибка HTTP: " + response.status);
  }
}

get_completed_achievements_num();