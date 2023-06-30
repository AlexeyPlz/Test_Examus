  // Функция получения куки по ключу
  const getCookie = (name) => {
    return document.cookie.split('; ').reduce((r, v) => {
      const parts = v.split('=')
      return parts[0] === name ? decodeURIComponent(parts[1]) : r
    }, '')
  }


  // Функция создания UUID
  const uuidv4 = () => {
    return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
      (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    )
  }


  // Изменение количества порций в куки
  const change_order_count = (id, new_count) => {
    let cookie_order = getCookie('order')
    let dict_order = !cookie_order ? new Object() : JSON.parse(cookie_order)
    if (new_count === 0) {
      delete dict_order[id]
    }
    if (new_count !== 0) {
      dict_order[id] = new_count
    }
    document.cookie = `order=${JSON.stringify(dict_order)}`
  }

  // Основные параметры
  let select = document.querySelector('.main_select')
  let list_card = document.querySelectorAll('.main_content_card')
  let plus_list = document.querySelectorAll('#plus')
  let minus_list = document.querySelectorAll('#minus')
  let cookie_order = getCookie('order')


  // Проверка UUID девайса в куки и его создание
  if (!getCookie('device')) { document.cookie = `device=${uuidv4()}`}


  // Установка значений количества порций на основе данных из куки
  if (cookie_order) {
    let dict_order = JSON.parse(cookie_order)
    for (let [dish_id, count] of Object.entries(dict_order)) {
      document.querySelector(`#ID-${dish_id}`).innerHTML = count
    }
  }


  // Создание слушателей на добавление порции блюда
  for (let plus of plus_list) {
    plus.addEventListener("click", function() {
      let count = document.querySelector(`#ID-${plus.value}`).innerHTML
      if (count !== '10') {
        let new_count = Number(count) + 1
        change_order_count(String(plus.value), new_count)
        document.querySelector(`#ID-${plus.value}`).innerHTML = new_count
      }
      if (count === '10') {
        alert("Нельзя сделать порцию больше 10.")
      }
    })
  }


  // Создание слушателей на удаление порции блюда
  for (let minus of minus_list) {
    minus.addEventListener("click", function() {
      let count = document.querySelector(`#ID-${minus.value}`).innerHTML
      if (count !== '0') {
        let new_count = Number(count) - 1
        change_order_count(String(minus.value), new_count)
        document.querySelector(`#ID-${minus.value}`).innerHTML = new_count
      }
      if (count === '0') {
        alert("Нельзя сделать порцию меньше 0.")
      }
    })
  }
 

  // Создание слушателя на выбор категории
  select.addEventListener("click", function(event) {
    let element = event.target
    let value = element.value
    for (let card of list_card) { card.style.display = ''}
    if (value !== 'Все блюда') {
      for (let card of list_card) {
        if (card.getAttribute('value') !== value) {
          card.style.display = 'none'
        }
      }
    }
  })