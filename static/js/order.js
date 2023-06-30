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

  // Проверка UUID девайса в куки и его создание
  if (!getCookie('device')) { document.cookie = `device=${uuidv4()}`}

  // Основные параметры
  let cookie_order = getCookie('order')
  let list_card = document.querySelectorAll('.main_content_card')
  let order_button = document.querySelector('.main_make_order')
  let total = 0

  // Установка значений количества порций и суммы
  if (cookie_order) {
    let dict_order = JSON.parse(cookie_order)
    for (let [dish_id, count] of Object.entries(dict_order)) {
      document.querySelector(`#ID2-${dish_id}`).innerHTML = count
      total += Number(document.querySelector(`#ID1-${dish_id}`).innerHTML) * Number(count)
    }
    document.querySelector('#total').innerHTML = total
  }