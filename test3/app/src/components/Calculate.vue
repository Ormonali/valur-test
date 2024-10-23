<template>
  <div class="calculate">
    <input type="number" v-model="first_value" :label="'First Value'">
    <p>*</p>
    <input type="number" v-model="second_value" :label="'Second Value'">
    <button @click="calculate">Calculate</button>
    <p>{{ result }}</p>
    <p>{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CalculateComponent',
  data() {
    return {
      first_value: '',
      second_value: '',
      result: '',
      error: '',
    }
  },
  methods: {
    calculate() {
      axios.post(
        'http://127.0.0.1:8000/api/calculate', {
        first_value: this.first_value,
        second_value: this.second_value,
      }).then(response => {
        if(response.data.error) {
          this.error = response.data.error
        }else{
          this.result = response.data.result
        }
      })
    }
  }
}
</script>

<style scoped>
.calculate {
  display: flex;
  flex-direction: column;
  align-items: center;
}
button {
  margin-top: 10px;
}
</style>
