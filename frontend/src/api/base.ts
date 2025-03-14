const getCookieValue = (name: string) =>
  document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || ''

export abstract class BaseApi {
  abstract getBaseUrl(): URL

  protected async sendGETRequest(url: URL) {
    const options = { method: 'GET' }
    return this.sendRequest(url, options)
  }

  protected async sendPOSTRequest(url: URL, data: object) {
    const options = {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
        'x-csrftoken': getCookieValue('csrftoken')
      }
    }
    return this.sendRequest(url, options)
  }

  protected async sendPOSTFormDataRequest(url: URL, formData: FormData) {
    const options = {
      method: 'POST',
      body: formData,
      headers: {
        'x-csrftoken': getCookieValue('csrftoken')
      }
    }
    return this.sendRequest(url, options)
  }

  protected async sendPUTRequest(url: URL, data?: object) {
    const options = {
      method: 'PUT',
      body: JSON.stringify(data || {}),
      headers: {
        'Content-Type': 'application/json',
        'x-csrftoken': getCookieValue('csrftoken')
      }
    }
    return this.sendRequest(url, options)
  }

  protected async sendPATCHRequest(url: URL, data?: object) {
    const options = {
      method: 'PATCH',
      body: JSON.stringify(data || {}),
      headers: {
        'Content-Type': 'application/json',
        'x-csrftoken': getCookieValue('csrftoken')
      }
    }
    return this.sendRequest(url, options)
  }

  protected async sendDELETERequest(url: URL) {
    const options = {
      method: 'DELETE',
      headers: {
        'x-csrftoken': getCookieValue('csrftoken')
      }
    }
    return this.sendRequest(url, options)
  }

  private async sendRequest(url: URL, options: object) {
    return fetch(url.href, options).then((response) => {
      if (response.ok && response.status !== 204) {
        return response.json().then((data) => data)
      } else if (response.status === 204) {
        return Promise.resolve(null)
      } else if ([400, 405].includes(response.status)) {
        return response.json().then((data) => Promise.reject(data))
      } else if ([403, 404].includes(response.status)) {
        return Promise.reject(response.status)
      }
    })
  }
}
