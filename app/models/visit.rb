class Visit < ActiveRecord::Base
  def self.base_url_for(url)
    parsed_url = Domainatrix.parse(url)

    "#{parsed_url.domain}.#{parsed_url.public_suffix}"
  end
end
