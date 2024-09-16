<template>
    <div>
        <input v-model="picked" placeholder="Введите ссылку или public key" />
        
        <my-button @click="getData(picked)">Получить данные по ссылке</my-button>
        
        <div v-if="data_flag">
            
            <span>{{ data.name }} - {{ data.type }}</span>
            <div class="divider"></div>
            
            <div v-for="item in data._embedded.items" :key="item">
                <div class="card-panel">
                    <div class="row">
                        <div class="col s2"><span class="brown-text text-lighten 1">{{ item.name }}</span></div>
                        <div class="col s2" v-if="item.type==='file'">
                            <i class=" Medium material-icons  yellow-text text-darken-4 point " @click="download(item.file)">file_download</i></div> 
                        <div class="col s2" v-else>
                            <i class=" Medium material-icons  yellow-text text-darken-4  " >folder</i></div> 
                    </div> 
                </div>
                 
            <br>
            </div>
        </div>
        <my-dialog v-model:show="isInfoBip" style="white-space: pre-wrap;">
        <h5 style="color: teal">{{ text }}  </h5>
        </my-dialog>
        
        <my-loader v-if="isLoader"></my-loader>
    </div>
</template>

<script>
import $api from '@/http'
import {mapState} from 'vuex'
export default {
    computed: mapState({
        isAuth: state=> state.isAuth,
    }),
    data: ()=>{
        return {
            data: {},
            picked: '',
            isInfoBip: false,
            isLoader: false,
            data_flag: false
        }
    },
   methods:{
    async getData(arg) {
            try {
                if (!arg){
                this.text = 'Введите ссылку или public key'
                this.isInfoBip = true
                return
            }
            this.isLoader = true
            const response = await $api.get(`api/yadisk/?arg=${arg}`)
            
            this.data = response.data.res
            console.log(this.data);
            this.data_flag = true
            this.isLoader = false
            } 
            catch (error) {
                                this.isLoader = false
                                this.text = `Ошибка выполнения - ${error}`
                                this.isInfoBip = true
                            }     
    },
    download(url) {
        window.location = url; // И загрузка начинается!
    }

}
}
</script>

<style scoped>
.point {
    cursor: pointer;
}
</style>