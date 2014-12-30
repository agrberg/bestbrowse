class Visit < ActiveRecord::Base
  def base_url
    URI(self.url).hostname
  end
end
