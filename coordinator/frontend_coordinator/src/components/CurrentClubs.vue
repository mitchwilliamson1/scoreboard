<template>
  <div class="hello">
  <div class="container row">
    <div v-for="club, i in clubs" :key="i" class="col-3">
      <div class="shadow p-2 mb-1 bg-body rounded"
        data-bs-toggle="collapse" 
        :data-bs-target="'#collapseClub'+i" 
        aria-expanded="false" 
        aria-controls="collapseOne">
        <div class="">
          <img class="logo" :src="'http://127.0.0.1:8000/players/get_logo/'+club.logo" >
        </div>
      </div>
      <div class="p-2">
        <div class="col collapse"
          :id="'collapseClub'+i"
          data-parent="#accordion">
          <edit-clubs @reLoadClubs="reLoadClubs" :club="club"/>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import { reactive, onMounted } from "vue";
import EditClubs from '../components/EditClubs.vue'


export default {
  name: 'CurrentPlayers',
  components: {
    EditClubs
  },
  props: {
    clubs: Object,
  },

  setup(props, context) {
    const state = reactive({
      someData: null,
    });

    function reLoadClubs() {
      context.emit("reLoadSponsors")
    }

    onMounted(async () => {});

    return {
      state,
      reLoadClubs
    };
  },
  data(){
    return{
      isActive: false,
    }
  },
  created () {
  },
  mounted () {
  },

  computed: {

  },

  methods:{
    post() {
      (async () => {
      const rawResponse = await fetch('http://127.0.0.1:8000/save', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        mode: 'no-cors',
        body: JSON.stringify(this.state)
      })
      const content = await rawResponse.json();
      console.log(content);
      })();
    },
    edit(game) {
      console.log(game)
    },
  },
}
</script>

<style scoped>

.flex-container {
  display: flex;
  justify-content: space-around;
}

.flex-child-spend {
  background-color: #b8fcbb;
  flex-grow: 1;
  border: 2px solid grey;
  margin: 5px;
  margin-top: 50px;
  margin-bottom: 80px;
  padding-bottom: 10px;
}

.flex-child {
  background-color: #e6dfcc;
  flex-grow: 1;
  border: 2px solid grey;
  margin: 2px;
}

.logo {
  aspect-ratio: 4/3;
  width: 50%;
  display: block;
  margin-left: auto;
  margin-right: auto;
}



input {
  width: 90%;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
