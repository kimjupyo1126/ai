const obj = {
  name: 'Alice',
  
  // 일반 함수: 자신만의 this를 가짐
  regularFunc: function() {
    console.log(this.name); // 'Alice'
  },
  
  // 화살표 함수: 상위 스코프의 this를 상속
  arrowFunc: () => {
    console.log(this.name); // undefined (또는 전역 객체)
  }
};

obj.regularFunc(); // 'Alice'
obj.arrowFunc();   // undefined
