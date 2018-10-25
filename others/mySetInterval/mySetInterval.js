//setInterval using setTimeout
function mySetInterval(fn, time) {
  let id = null;
  fn();
  _helper();

  function _helper() {
    if (id) {
      clearTimeout(id);
    }
    id = setTimeout(() => {
      fn();
      _helper();
    }, time);
  }
}

// with myClearInterval
// global id
let globalIntervalId = 0;

function mySetInterval(fn, time) {
  if (!window.myIntervalIds) {
    window.myIntervalIds = {};
  }
  // timeout Id
  let timeoutId = null;

  // interval id
  const intervalId = globalIntervalId++;
  window.myIntervalIds[intervalId] = true;

  // 1st call
  fn();
  _helper();

  return intervalId;


  function _helper() {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }
    if (window.myIntervalIds[intervalId]) {
      timeoutId = setTimeout(() => {
        fn();
        _helper();
      }, time);
    }
  }
}

function myClearInterval(id) {
  delete window.myIntervalIds[id];
}
