# 个人主页

基于 HTML + TailwindCSS + JavaScript 的静态个人主页。

## 特性

- ✅ 响应式设计
- ✅ 深浅主题切换（自动/手动）
- ✅ 平滑滚动导航
- ✅ GitHub Actions 自动部署
- ✅ 可扩展插件支持（预留 Three.js 等扩展接口）

## 项目结构

```
.
├── .github/workflows/    # GitHub Actions 配置
├── src/
│   ├── index.html        # 主页面
│   ├── css/
│   │   ├── input.css     # TailwindCSS 输入
│   │   └── output.css    # 生成的 CSS
│   ├── js/
│   │   ├── main.js       # 主逻辑
│   │   └── theme.js      # 主题切换
│   └── assets/
│       └── images/       # 图片资源
├── package.json          # npm 配置
└── tailwind.config.js    # TailwindCSS 配置
```

## 本地开发

```bash
# 安装依赖
npm install

# 开发模式（自动编译 CSS）
npm run dev

# 构建（生成 dist 目录）
npm run build

# 预览
npm run preview
```

## 部署

1. Fork 本仓库
2. 在仓库设置中启用 GitHub Pages（Source 选择 GitHub Actions）
3. 推送代码到 main 分支即可自动部署

## 自定义

- 修改 `src/index.html` 替换内容
- 修改 `src/css/input.css` 自定义样式
- 添加插件：在 `src/js/` 创建新文件并在 HTML 中引入
