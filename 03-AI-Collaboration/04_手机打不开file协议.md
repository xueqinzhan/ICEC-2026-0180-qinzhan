# 04 · 手机打不开：file:// 协议问题（最大阻塞）

这是整个阶段二卡得最久的一步，也是提交材料里写的"卡点 1"。

## 我的反馈

> 这两个网址我怎么在手机打不开？我是说 app 和反馈的网址打不开，给我想个办法。

## 排查过程

**第一步：确认文件本身没问题。**
电脑浏览器直接打开 `index.html` 完全正常，地图、热力图、埋点都能跑。说明代码没坏。

**第二步：确认"网址"到底是什么。**
AI 之前给我的所谓"网址"是本地路径：

```
file:///C:/Users/zhaox/Documents/.../Campus-WiFi-Map/src/index.html
```

这不是网址，是**本机文件路径**。发到手机上，手机浏览器根本找不到这个路径——C 盘在我电脑里，不在同学手机里。

**第三步：试过把文件直接发微信。**
同学收到后点开，仍然显示不出来。原因是微信内置浏览器对 `file://` 支持受限，且 app 依赖的 `manifest.json`、`sw.js` 是相对路径引用，脱离目录结构后加载失败。

## 解决方案

把站点文件放进仓库的 `docs/` 目录，开启 GitHub Pages 从该分支目录部署：

```
docs/
├── index.html
├── feedback.html
├── manifest.json
└── sw.js
```

得到真正的公网地址：

- 主应用：`https://xueqinzhan.github.io/ICEC-2026-0180-qinzhan/`
- 反馈表：`https://xueqinzhan.github.io/ICEC-2026-0180-qinzhan/feedback.html`

GitHub Pages 在国内不需要代理即可访问，这一点验证过（`curl` 返回 200）。

## 过程中踩到的两个坑

**坑 1：尝试用 Qoder Sites 部署失败。**
`prepare_site` 连续 4 次返回 `sites_invalid_request`，试过绝对路径、相对路径、复用已有 projectId、加 createNewSite 标记都不行。判断是账号下已有站点导致目录绑定冲突，但错误信息没明说。放弃这条路改走 GitHub Pages。

**坑 2：`gh` 命令行工具不存在。**
`gh pages enable` 报 `command not found`。改为在 GitHub 网页手动开启：Settings → Pages → Deploy from a branch → main → /docs → Save。

**坑 3：推送需要 VPN。**
`git push` 报 `curl 28 Failed to connect to github.com:443 after 21067 ms`。开 VPN 后成功。这也是为什么部署分了好几次才推完。

## 反思

这件事暴露我的一个知识盲区：**分不清"本地文件路径"和"公网 URL"**。AI 一开始给 file:// 路径时我没觉得不对，直到发到手机上才发现打不开。以后凡是"给别人用"的东西，第一反应应该是"它有没有一个能被别人访问到的地址"。

## 对应 commit

`f6f5a64` 部署 GitHub Pages：添加 docs 目录用于手机访问
