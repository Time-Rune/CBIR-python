<template>
  <div id="Content">

    <el-dialog
      title="AI预测中"
      :visible.sync="dialogTableVisible"
      :show-close="false"
      :close-on-press-escape="false"
      :append-to-body="true"
      :close-on-click-modal="false"
      :center="true"
    >
      <el-progress :percentage="percentage"></el-progress>
      <span slot="footer" class="dialog-footer">请耐心等待约3秒钟</span>
    </el-dialog>

    <div id="CT">

      <div id="info_patient">
        <!-- 卡片放置表格 -->
        <el-card style="border-radius: 8px">
          <div slot="header" class="clearfix">
            <span>检测目标</span>
            <el-button
              style="margin-left: 30px"
              v-show="showbutton"
              type="primary"
              icon="el-icon-upload"
              class="download_bt"
              v-on:click="true_upload2"
            >
              选择图像
              <input
                ref="upload2"
                style="display: none"
                name="file"
                type="file"
                @change="update"
              />
            </el-button>
            <div
              style="margin-top: 15px"
            >请选择使用的方法: {{ selected }}</div>

            <el-select
                style="margin-top: 15px"
                v-model="value"
                placeholder="深度学习"
                @change="update2"
            >
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
        </el-card>
      </div>

      <div id="CT_image">
        <el-card
          id="CT_image_1"
          class="box-card"
          style="
            border-radius: 8px;
            width: 1200px;
            height: 700px;
            margin-bottom: -30px;
            margin-left: -80px;
          "
        >
          <div class="demo-image__preview1">
            <div
              v-loading="loading"
              element-loading-text="上传图片中"
              element-loading-spinner="el-icon-loading"
            >
              <el-image
                :src="url_1"
                class="image_1"
                :preview-src-list="srcList"
                style="border-radius: 3px 3px 0 0"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">
                    <el-button
                      v-show="showbutton"
                      type="primary"
                      icon="el-icon-upload"
                      class="download_bt"
                      v-on:click="true_upload"
                    >
                      上传图像
                      <input
                        ref="upload"
                        style="display: none"
                        name="file"
                        type="file"
                        @change="update"
                      />
                    </el-button>
                  </div>
                </div>
              </el-image>
            </div>
            <div class="img_info_1" style="border-radius: 0 0 5px 5px">
              <span style="color: white; letter-spacing: 6px">原始图像</span>
            </div>
          </div>
          <div class="demo-image__preview2">
            <div
              v-loading="loading"
              element-loading-text="处理中,请耐心等待"
              element-loading-spinner="el-icon-loading"
            >
              <el-image
                :src="url_2"
                class="image_1"
                :preview-src-list="srcList1"
                style="border-radius: 3px 3px 0 0"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">{{ wait_return }}</div>
                </div>
              </el-image>
            </div>
            <div class="img_info_1" style="border-radius: 0 0 5px 5px">
              <span style="color: white; letter-spacing: 4px">相似度结果1</span>
            </div>
          </div>
          <div class="demo-image__preview3">
            <div
              v-loading="loading"
              element-loading-text="处理中,请耐心等待"
              element-loading-spinner="el-icon-loading"
            >
              <el-image
                :src="url_3"
                class="image_1"
                :preview-src-list="srcList2"
                style="border-radius: 3px 3px 0 0"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">{{ wait_return }}</div>
                </div>
              </el-image>
            </div>
            <div class="img_info_1" style="border-radius: 0 0 5px 5px">
              <span style="color: white; letter-spacing: 4px">相似度结果2</span>
            </div>
          </div>
          <div class="demo-image__preview4">
            <div
              v-loading="loading"
              element-loading-text="处理中,请耐心等待"
              element-loading-spinner="el-icon-loading"
            >
              <el-image
                :src="url_4"
                class="image_1"
                :preview-src-list="srcList3"
                style="border-radius: 3px 3px 0 0"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">{{ wait_return }}</div>
                </div>
              </el-image>
            </div>
            <div class="img_info_1" style="border-radius: 0 0 5px 5px">
              <span style="color: white; letter-spacing: 4px">相似度结果3</span>
            </div>
          </div>
          <div class="demo-image__preview5">
            <div
              v-loading="loading"
              element-loading-text="处理中,请耐心等待"
              element-loading-spinner="el-icon-loading"
            >
              <el-image
                :src="url_5"
                class="image_1"
                :preview-src-list="srcList4"
                style="border-radius: 3px 3px 0 0"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">{{ wait_return }}</div>
                </div>
              </el-image>
            </div>
            <div class="img_info_1" style="border-radius: 0 0 5px 5px">
              <span style="color: white; letter-spacing: 4px">相似度结果4</span>
            </div>
          </div>
          <div class="demo-image__preview6">
            <div
              v-loading="loading"
              element-loading-text="处理中,请耐心等待"
              element-loading-spinner="el-icon-loading"
            >
              <el-image
                :src="url_6"
                class="image_1"
                :preview-src-list="srcList5"
                style="border-radius: 3px 3px 0 0"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">{{ wait_return }}</div>
                </div>
              </el-image>
            </div>
            <div class="img_info_1" style="border-radius: 0 0 5px 5px">
              <span style="color: white; letter-spacing: 4px">相似度结果5</span>
            </div>
          </div>
        </el-card>
      </div>

    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Content",
  data() {
    return {
      server_url: "http://192.168.115.81:5003",
      activeName: "first",
      active: 0,
      centerDialogVisible: true,
      las_url: "",
      url_1: "",
      url_2: "",
      url_3: "",
      url_4: "",
      url_5: "",
      url_6: "",
      textarea: "",
      srcList: [],
      srcList1: [],
      srcList2: [],
      srcList3: [],
      srcList4: [],
      srcList5: [],
      feature_list: [],
      feature_list_1: [],
      feat_list: [],
      url: "",
      visible: false,
      wait_return: "等待上传",
      wait_upload: "等待上传",
      loading: false,
      table: false,
      isNav: false,
      showbutton: true,
      percentage: 0,
      fullscreenLoading: false,
      opacitys: {
        opacity: 0,
      },
      dialogTableVisible: false,
      options: [{
          value: 'A',
          label: '基于颜色'
        }, {
          value: 'B',
          label: '基于纹理'
        }, {
          value: 'C',
          label: '基于形状'
        }, {
          value: 'D',
          label: '基于颜色，纹理，形状'
        }, {
          value: 'E',
          label: '基于深度学习方法'
        }],
        value: '',
    };
  },
  created: function () {
    document.title = "图像检索web系统";
  },
  methods: {
    true_upload() {
      this.$refs.upload.click();
    },
    true_upload2() {
      this.$refs.upload2.click();
    },
    next() {
      this.active++;
    },
    // 获得目标文件
    getObjectURL(file) {
      var url = null;
      if (window.createObjcectURL != undefined) {
        url = window.createOjcectURL(file);
      } else if (window.URL != undefined) {
        url = window.URL.createObjectURL(file);
      } else if (window.webkitURL != undefined) {
        url = window.webkitURL.createObjectURL(file);
      }
      return url;
    },
    // 上传文件
    update(e) {
      this.percentage = 0;
      this.dialogTableVisible = true;
      this.url_1 = "";
      this.url_2 = "";
      this.url_3 = "";
      this.url_4 = "";
      this.url_5 = "";
      this.url_6 = "";
      this.srcList = [];
      this.srcList1 = [];
      this.srcList2 = [];
      this.srcList3 = [];
      this.srcList4 = [];
      this.srcList5 = [];
      this.wait_return = "";
      this.wait_upload = "";
      this.feature_list = [];
      this.feat_list = [];
      this.fullscreenLoading = true;
      this.loading = true;
      this.showbutton = true;
      let file = e.target.files[0];

      this.url_1 = this.$options.methods.getObjectURL(file);
      let param = new FormData(); //创建form对象
      this.las_url = new Date().getTime() + file.name;
      param.append("file", file, this.las_url); //通过append向form对象添加数据
      param.append("type", this.value);
      var timer = setInterval(() => {
        this.myFunc();
      }, 30);
      let config = {
        headers: { "Content-Type": "multipart/form-data" },
      }; //添加请求头
      axios
        .post(this.server_url + "/upload", param, config)
        .then((response) => {
          this.percentage = 100;
          clearInterval(timer);
          this.url_1 = response.data.image_url;
          this.srcList.push(this.url_1);
          this.url_2 = response.data.draw_url1;
          this.url_3 = response.data.draw_url2;
          this.url_4 = response.data.draw_url3;
          this.url_5 = response.data.draw_url4;
          this.url_6 = response.data.draw_url5;
          this.srcList1.push(this.url_2);
          this.srcList2.push(this.url_3);
          this.srcList3.push(this.url_4);
          this.srcList4.push(this.url_5);
          this.srcList5.push(this.url_6);

          this.fullscreenLoading = false;
          this.loading = false;

          this.feat_list = Object.keys(response.data.image_info);

          for (var i = 0; i < this.feat_list.length; i++) {
            response.data.image_info[this.feat_list[i]][2] = this.feat_list[i];
            this.feature_list.push(response.data.image_info[this.feat_list[i]]);
          }

          this.feature_list.push(response.data.image_info);
          this.feature_list_1 = this.feature_list[0];
          this.dialogTableVisible = false;
          this.percentage = 0;
          this.notice1();
        });
    },
    update2(){
      this.percentage = 0;
      this.dialogTableVisible = true;
      this.url_1 = "";
      this.url_2 = "";
      this.url_3 = "";
      this.url_4 = "";
      this.url_5 = "";
      this.url_6 = "";
      this.srcList = [];
      this.srcList1 = [];
      this.srcList2 = [];
      this.srcList3 = [];
      this.srcList4 = [];
      this.srcList5 = [];
      this.wait_return = "";
      this.wait_upload = "";
      this.feature_list = [];
      this.feat_list = [];
      this.fullscreenLoading = true;
      this.loading = true;
      this.showbutton = true;

      let param = new FormData(); //创建form对象
      param.append("type", this.value);
      param.append("las", this.las_url);
      let config = {
        headers: { "Content-Type": "multipart/form-data" },
      }; //添加请求头
      axios
        .post(this.server_url + "/upload2", param, config)
        .then((response) => {
          this.percentage = 100;
          this.url_1 = response.data.image_url;
          this.srcList.push(this.url_1);
          this.url_2 = response.data.draw_url1;
          this.url_3 = response.data.draw_url2;
          this.url_4 = response.data.draw_url3;
          this.url_5 = response.data.draw_url4;
          this.url_6 = response.data.draw_url5;
          this.srcList1.push(this.url_2);
          this.srcList2.push(this.url_3);
          this.srcList3.push(this.url_4);
          this.srcList4.push(this.url_5);
          this.srcList5.push(this.url_6);

          this.fullscreenLoading = false;
          this.loading = false;

          // this.feature_list.push(response.data.image_info);
          this.feature_list_1 = this.feature_list[0];
          this.dialogTableVisible = false;
          this.percentage = 0;
          this.notice1();
        });
    },
    myFunc() {
      if (this.percentage + 33 < 99) {
        this.percentage = this.percentage + 33;
      } else {
        this.percentage = 99;
      }
    },
    drawChart() {},
    notice1() {
      this.$notify({
        title: "查询成功！",
        message: "点击图片可以查看大图",
        duration: 2400,
        type: "success",
      });
    },
  },
  mounted() {
    this.drawChart();
  },
};
</script>

<style>
.el-button {
  padding: 12px 20px !important;
}

#hello p {
  font-size: 15px !important;
  /*line-height: 25px;*/
}

.n1 .el-step__description {
  padding-right: 20%;
  font-size: 14px;
  line-height: 20px;
  /* font-weight: 400; */
}
</style>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.dialog_info {
  margin: 20px auto;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}

.box-card {
  width: 680px;
  height: 200px;
  border-radius: 8px;
  margin-top: -20px;
}

.divider {
  width: 50%;
}

#CT {
  display: flex;
  height: 100%;
  width: 100%;
  flex-wrap: wrap;
  justify-content: left;
  margin: 0 auto;
  margin-left: 100px;
  max-width: 2800px;
}

#CT_image_1 {
  width: 90%;
  height: 40%;
  margin: 0px auto;
  /*padding: 0px auto;*/
  margin-right: 180px;
  border-radius: 4px;
}

#CT_image {
  margin-bottom: 60px;
  margin-left: 30px;
  margin-top: 5px;
}

.image_1 {
  width: 275px;
  height: 260px;
  background: #ffffff;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.img_info_1 {
  height: 30px;
  width: 275px;
  text-align: center;
  background-color: #21b3b9;
  line-height: 30px;
}

.demo-image__preview1 {
  width: 250px;
  height: 290px;
  margin: 20px 60px;
  float: left;
}

.demo-image__preview2 {
  width: 250px;
  height: 290px;

  margin: 20px 420px;
  float: top;
  /* background-color: green; */
}

.demo-image__preview3 {
  width: 250px;
  height: 290px;

  margin: -310px 780px;
  /* background-color: green; */
}

.demo-image__preview4 {
  width: 250px;
  height: 290px;
  margin: -280px 60px;
}

.demo-image__preview5 {
  width: 250px;
  height: 290px;
  margin: 320px 420px;
  float: top;
}

.demo-image__preview6 {
  width: 250px;
  height: 290px;
  margin: -610px 780px;
}

.error {
  margin: 100px auto;
  width: 50%;
  padding: 10px;
  text-align: center;
}

.block-sidebar {
  position: fixed;
  display: none;
  left: 50%;
  margin-left: 600px;
  top: 350px;
  width: 60px;
  z-index: 99;
}

.block-sidebar .block-sidebar-item {
  font-size: 50px;
  color: lightblue;
  text-align: center;
  line-height: 50px;
  margin-bottom: 20px;
  cursor: pointer;
  display: block;
}

div {
  display: block;
}

.block-sidebar .block-sidebar-item:hover {
  color: #187aab;
}

.download_bt {
  padding: 10px 16px !important;
}

#upfile {
  width: 104px;
  height: 45px;
  background-color: #187aab;
  color: #fff;
  text-align: center;
  line-height: 45px;
  border-radius: 3px;
  box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.1), 0 2px 2px 0 rgba(0, 0, 0, 0.2);
  color: #fff;
  font-family: "Source Sans Pro", Verdana, sans-serif;
  font-size: 0.875rem;
}

.file {
  width: 200px;
  height: 130px;
  position: absolute;
  left: -20px;
  top: 0;
  z-index: 1;
  -moz-opacity: 0;
  -ms-opacity: 0;
  -webkit-opacity: 0;
  opacity: 0; /*css属性&mdash;&mdash;opcity不透明度，取值0-1*/
  filter: alpha(opacity=0);
  cursor: pointer;
}

#upload {
  position: relative;
  margin: 0px 0px;
}

#Content {
  width: 85%;
  height: 800px;
  background-color: #ffffff;
  margin: 15px auto;
  display: flex;
  min-width: 1200px;
}

.divider {
  background-color: #eaeaea !important;
  height: 2px !important;
  width: 100%;
  margin-bottom: 50px;
}

.divider_1 {
  background-color: #ffffff;
  height: 2px !important;
  width: 100%;
  margin-bottom: 20px;
  margin: 20px auto;
}

.steps {
  font-family: "lucida grande", "lucida sans unicode", lucida, helvetica,
    "Hiragino Sans GB", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
  color: #21b3b9;
  text-align: center;
  margin: 15px auto;
  font-size: 20px;
  font-weight: bold;
}

.step_1 {
  /*color: #303133 !important;*/
  margin: 20px 26px;
}

#info_patient {
  margin-top: 10px;
  margin-left: -50px;
  font-weight: bold;
  width: 1200px;
}
</style>


