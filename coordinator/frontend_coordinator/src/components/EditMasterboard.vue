<template>
  <div class="edit">
    <div class="card p-2 pt-0 shadow">

      <div class="row g-3">
        <div class="col-md-6">
          <label for="inputEmail4" class="form-label">Rink</label>
          <input type="text" class="form-control" id="inputEmail4" v-model="masterboard.masterboard">
        </div>
        <div class="col-md-6">
          <label for="inputPassword4" class="form-label">Ip Address</label>
          <input type="text" class="form-control" id="inputPassword4" v-model="masterboard.ip">
        </div>
        <div class="row">
          <div class="col">
            <div>Linked Rinks</div>
            <div v-for="ip, i in state.ips" class="form-check form-check-inline">
                <input class="form-check-input" type="checkbox" id="inlineCheckbox1" v-model="ip.show">
                <label class="form-check-label" for="inlineCheckbox1">{{ip.rink}}</label>
            </div>

            <div class="col-12">
              <button @click="updateMasterboard" type="submit" class="btn btn-primary">Update</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <br>
    

  </div>
</template>

<script>
import { reactive, onMounted } from "vue";
import axios from 'axios'

export default {
  name: 'EditMasterboards',
  props: {
    masterboard: Object,
    rinks: Object,
  },

  setup(props) {
    const state = reactive({
      ips: [],
    });

    var path = ""
    path = 'http://127.0.0.1:8000/games'

    onMounted(async () => {
      // getMasterboard()
      getIpList()
    });
    function getIpList() {
      var blah = props.masterboard.rink_ips.map(( e ) => {
        return e.rink_id
      });
      state.ips = props.rinks.map(( e ) => {
        e.show = blah.includes(e.rink_id)
        return {rink:e.rink, ip:e.ip, rink_id:e.rink_id, show:e.show}
      });
    }

    function getMasterboard() {
      axios.get(path+'/get_masterboard', 
        { params: { rink: props.masterboard.ip } })
      .then(function (response) {
        if (response.status == 200){
          state.ips = ['127.0.0.1:8080', '127.0.0.2:885']
          state.ips = response.data
        }
      })
      .catch(function (error) {
        console.log("ERROR ", error);
      })
      .then(function () {

      });
    }

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
    updateMasterboard() {
      (async () => {
      const rawResponse = await fetch(this.path+'/update_masterboards', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        mode: 'no-cors',
        body: JSON.stringify({masterboard:this.masterboard, ips:this.state.ips})
      })
      const content = await rawResponse.json();
      console.log(content);
      })();
    },
    addRemove(ip){
      console.log(ip)
      this.state.ips.push(ip)
    },
    addIP(){
      this.state.ips.push("")
    },
    removeIP(key){
      this.state.ips.splice(key, 1)
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
