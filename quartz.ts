import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { MnrnSiteTransforms } from "./mnrn-transforms"

const config = await loadQuartzConfig()
config.plugins.transformers.push(MnrnSiteTransforms)
export default config
export const layout = await loadQuartzLayout()
