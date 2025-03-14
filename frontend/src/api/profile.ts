import { BaseApi } from '@/api/base'

import type { Profile } from '@/interfaces/models'

export class ProfileApi extends BaseApi {
  getBaseUrl(): URL {
    const backendURL = new URL(window.location.href)
    backendURL.pathname = '/api/profile/'
    return backendURL
  }

  async create(profileData: FormData): Promise<Profile> {
    return this.sendPOSTFormDataRequest(this.getBaseUrl(), profileData)
  }

  async retrieveProfileList(): Promise<Profile[]> {
    return this.sendGETRequest(this.getBaseUrl())
  }
}
