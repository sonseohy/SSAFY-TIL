<p>{{ }}<p>
<p v-html=""> </p>

- 양방향 바인드 (출력/입력)
<input v-model="">

- 단방향 바인드 (출력)
<p v-bind:id=""> </p>
<a :href=""> </a>

- 이벤트 입력 (입력)
<input v-on:input="">
<button @click="">
<form @submit.prevent="">

- 클래스 변경 (v-bind 사용)
<div :class=""></div>
<div :class="{active: isActive}"></div>
<div :class="{active: num>10}"></div>
<div :class="[,]"></div>