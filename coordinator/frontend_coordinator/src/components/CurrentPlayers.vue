<template>
  <div class="hello">
  <div class="container">
    <div class="row">
      <div class="col fw-bold">Club</div>
      <div class="col fw-bold">First Name</div>
      <div class="col fw-bold">Last Name</div>
      <div class="col fw-bold">Bowls Number</div>
      <div class="col fw-bold">Grade</div>
    </div>
    <div v-if="players && clubs" v-for="player, i in players" :key="i">
      <div class="row shadow p-2 mb-1 bg-body rounded"
        data-bs-toggle="collapse" 
        :data-bs-target="'#collapse'+i" 
        aria-expanded="false" 
        aria-controls="collapseOne">
      <div class="col">{{clubName(player.club)}}</div>
      <div class="col">{{player.first_name}}</div>
      <div class="col">{{player.last_name}}</div>
      <div class="col">{{player.bowls_number}}</div>
      <div class="col">{{player.grade}}</div>
      </div>
      <div class="row p-2">
        <div class="col collapse"
          :id="'collapse'+i"
          data-parent="#accordion">
          <edit-player :clubs="clubs" :player="player"/>
        </div>
        
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import { reactive, onMounted } from "vue";
import EditPlayer from '../components/EditPlayer.vue'


export default {
  name: 'CurrentPlayers',
  components: {
    EditPlayer
  },
  props: {
    players: Object,
    clubs: Object,
  },

  setup() {
    const state = reactive({
      someData: null,
    });

    var path = ""
    path = 'http://127.0.0.1:8000/budget'

    onMounted(async () => {});

    return {
      path,
      state
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
    clubName(playerClub){
      var club = this.clubs.filter(i => i.club_id == playerClub)
      return club[0]['club_name']
    },
    post() {
      (async () => {
      const rawResponse = await fetch(this.path+'/save', {
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
